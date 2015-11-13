# Haze
#
# Author: Joe Block <jpb@unixorn.net>
# License: Apache 2.0

from setuptools import setup, find_packages

name = "haze"

setup(
  name = name,
  author = "Joe Block",
  author_email = "jpb@unixorn.net",
  description = "Haze is a collection of AWS utility functions",
  url = "https://github.com/unixorn/haze",
  packages = find_packages(),
  install_requires = [
    "boto==2.38.0"
  ],
  version = "0.0.8",
  download_url = 'https://github.com/unixorn/haze/tarball/0.0.8',
  keywords = ['aws', 'cloud'],
  entry_points = {
    "console_scripts": [
      "haze-aws-instance-id = %s.cli.awsinstanceid:awsInstanceID" % name,
      "haze-aws-read-metadata-key = %s.cli.awsmetadata:awsReadMetadataKey" % name,
      "haze-aws-region = %s.cli.awsregion:awsMyRegion" % name
    ]
  }
)
