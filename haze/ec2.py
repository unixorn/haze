# Author: Joe Block <jpb@unixorn.net>
# Copyright (c) 2015 Joe Block
# License: Apache 2.0
"""
Helper functions for use in ec2.
"""

import boto.ec2
import boto.utils


# metadata helper functions
def loadInstanceMetadata():
  """Loads the instance metadata for the instance we're running on

  :returns: instance metadata
  """
  return boto.utils.get_instance_metadata(timeout=1, num_retries=3)


def myInstanceID():
  """Determine the instance ID for the running instance

  :returns: instanceID
  :rtype: str
  """
  return loadInstanceMetadata()["instance-id"]


def myRegion():
  """Returns the region of the running instance

  :returns str: region
  :rtype: str
  """
  return loadInstanceMetadata()["placement"]["availability-zone"][:-1]


# Tag helpers
def readInstanceTag(instanceID, tagName="Name", connection=None):
  """
  Load a tag from EC2

  :param str instanceID: Instance ID to read the tag on
  :param str tagName: Name of tag to load
  :param connection: optional boto connection to use

  :returns: the tag's value
  :rtype: str
  """
  assert isinstance(instanceID, basestring), ("instanceID must be a string but is %r" % instanceID)
  assert isinstance(tagName, basestring), ("tagName must be a string but is %r" % tagName)

  if not connection:
    # Assume AWS credentials are in the environment or the instance is using an IAM role
    connection = boto.ec2.connect_to_region(myRegion())

  # Filter the tag values for our instance_id
  # http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/ApiReference-cmd-DescribeTags.html
  tagData = connection.get_all_tags(filters={"resource-id": instanceID, "key": tagName})
  if tagData:
    tagValue = tagData[0].value
  else:
    raise RuntimeError, "%s: No such tag on %s" % (tagName, instanceID)
  return tagValue


def readMyEC2Tag(tagName, connection=None):
  """
  Load an EC2 tag for the running instance & print it.

  :param str tagName: Name of the tag to read
  :param connection: Optional boto connection
  """
  assert isinstance(tagName, basestring), ("tagName must be a string but is %r" % tagName)

  # Load metadata. if == {} we are on localhost
  # http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html

  if not connection:
    # Assume AWS credentials are in the environment or the instance is using an IAM role
    connection = boto.ec2.connect_to_region(myRegion())

  print readInstanceTag(connection=connection,
                        instanceID=myInstanceID(),
                        tagName=tagName)
