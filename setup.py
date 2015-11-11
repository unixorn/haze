# Haze
#
# Author: Joe Block <jpb@unixorn.net>
# License: Apache 2.0

from setuptools import setup, find_packages

name = "haze"
requirements = map(str.strip, open("requirements.txt").readlines())

setup(
  name = name,
  author = "Joe Block",
  author_email = "jpb@unixorn.net",
  description = "Haze AWS utility functions",
  url = "https://github.com/unixorn/haze",
  packages = find_packages(),
  version = "0.0.5",
  download_url = 'https://github.com/unixorn/haze/tarball/0.0.5',
  keywords = ['aws', 'cloud'],
  install_requires = requirements,
  entry_points = {
    "console_scripts": [
      "aws-instance-id = %s.commands.myinstanceid:awsInstanceID" % name,
      ("aws-region = %s.commands.myregion:awsMyRegion" % name)
    ]
  }
)
