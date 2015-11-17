# Copyright 2015 Joe Block <jpb@unixorn.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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


def getMetadataKey(name):
  """
  Returns a given metadata key

  :param str name: Name of key to retrieve
  :returns: the value of the specified metadata key
  :rtype: str
  """
  return loadInstanceMetadata()[name]


def myAMIid():
  """Determine the AMI ID for the running instance

  :returns: ami ID
  :rtype: str
  """
  return loadInstanceMetadata()["ami-id"]


def myInstanceID():
  """Determine the instance ID for the running instance

  :returns: instanceID
  :rtype: str
  """
  return loadInstanceMetadata()["instance-id"]


def myInstanceType():
  """Determine the instance type of the running instance

  :returns: instance type
  :rtype: str
  """
  return loadInstanceMetadata()["instance-type"]


def myPublicIPv4():
  """Determine the public IP v4 for the running instance

  :returns: Instance's public IP v4
  :rtype: str
  """
  return loadInstanceMetadata()["public-ipv4"]


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
