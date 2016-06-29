#!/usr/bin/env python
#
# Haze
#
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
setup.py for haze
"""

import os
import shutil
from setuptools import setup, find_packages, Command

name = "haze"
version = "0.0.12"


class CleanCommand(Command):
  """
  Add a clean option to setup.py's commands
  """
  description = "Clean up"
  user_options = []


  def initialize_options(self):
    self.cwd = None


  def finalize_options(self):
    self.cwd = os.getcwd()


  def run(self):
    assert os.getcwd() == self.cwd, "Must be in package root: %s" % self.cwd
    if os.path.isdir("build"):
      shutil.rmtree("build")
    if os.path.isdir("dist"):
      shutil.rmtree("dist")



setup(
  name=name,
  author="Joe Block",
  author_email="jpb@unixorn.net",
  description="Haze is a collection of AWS utility functions",
  url="https://github.com/unixorn/haze",
  packages=find_packages(),
  install_requires=[
    "boto>=2.38.0",
    "logrus>=0.0.2"
  ],
  cmdclass={
    "clean": CleanCommand,
  },
  version=version,
  download_url="https://github.com/unixorn/haze/tarball/%s" % version,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Operating System :: POSIX",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 2.7",
    "Topic :: System :: Systems Administration",
  ],
  keywords=['aws', 'cloud'],
  entry_points={
    "console_scripts": [
      "haze = %s.cli.conductor:hazeDriver" % name,
      "haze-aws-ami-id = %s.cli.commands:awsAMIid" % name,
      "haze-aws-instance-id = %s.cli.commands:awsInstanceID" % name,
      "haze-aws-instance-type = %s.cli.commands:awsInstanceType" % name,
      "haze-aws-public-ipv4 = %s.cli.commands:awsPublicIPv4" % name,
      "haze-aws-read-metadata-key = %s.cli.awsmetadata:awsReadMetadataKey" % name,
      "haze-aws-region = %s.cli.commands:awsMyRegion" % name
    ]
  }
)
