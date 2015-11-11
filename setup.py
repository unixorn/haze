# Haze
#
# Author: Joe Block <jpb@unixorn.net>
# License: Apache 2.0

from setuptools import setup, find_packages

name = "haze"
requirements = map(str.strip, open("requirements.txt").readlines())

setup(
  name = name,
  description = "Haze AWS utility functions",
  packages = find_packages(),
  version = "0.0.3",
  install_requires = requirements,
  entry_points = {
    "console_scripts": [
      "aws-instance-id = %s.commands.myinstanceid:awsInstanceID" % name,
      ("aws-region = %s.commands.myregion:awsMyRegion" % name)
    ]
  }
)
