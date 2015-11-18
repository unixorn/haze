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

from setuptools import setup, find_packages

name = "haze"
version = "0.0.10"

setup(
  name = name,
  author = "Joe Block",
  author_email = "jpb@unixorn.net",
  description = "Haze is a collection of AWS utility functions",
  url = "https://github.com/unixorn/haze",
  packages = find_packages(),
  install_requires = [
    "boto==2.38.0",
    "logrus>=0.0.1"
  ],
  version = version,
  download_url = "https://github.com/unixorn/haze/tarball/%s" % version,
  keywords = ['aws', 'cloud'],
  entry_points = {
    "console_scripts": [
      "haze-aws-ami-id = %s.cli.commands:awsAMIid" % name,
      "haze-aws-instance-id = %s.cli.commands:awsInstanceID" % name,
      "haze-aws-instance-type = %s.cli.commands:awsInstanceType" % name,
      "haze-aws-public-ipv4 = %s.cli.commands:awsPublicIPv4" % name,
      "haze-aws-read-metadata-key = %s.cli.awsmetadata:awsReadMetadataKey" % name,
      "haze-aws-region = %s.cli.commands:awsMyRegion" % name
    ]
  }
)
