# Haze
#
# Author: Joe Block <jpb@unixorn.net>
# License: Apache 2.0

from setuptools import setup, find_packages

requirements = map(str.strip, open("requirements.txt").readlines())

setup(
  name = "haze",
  packages = find_packages(),
  version = "0.0.1",
  install_requires = requirements
)
