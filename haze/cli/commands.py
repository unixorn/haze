#!/usr/bin/env python
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
There are a lot of properties for a given instance in EC2 that have
turned out to be really handy to access from bash scripts running on
the instance.

Trying to parse them directly in bash is more hassle than it is worth,
and I've written some of these toy attribute readers three or four times
because previous jobs never open sourced them.

Rewriting some of these handy attribute readers one last time in an Apache
licensed python module.
"""

import haze.ec2

# Bash helpers
def awsAMIid():
  """Print a running instance's AMI ID"""
  print haze.ec2.myAMIid()


def awsInstanceID():
  """Print a running instance's instance ID"""
  print haze.ec2.myInstanceID()


def awsInstanceType():
  """Print a running instance's instance type"""
  print haze.ec2.myInstanceType()


def awsMyRegion():
  """Print a running instance's AWS region"""
  print haze.ec2.myRegion()


def awsPublicIPv4():
  """Print a running instance's AMI ID"""
  print haze.ec2.myPublicIPv4()



if __name__ == "__main__":
  awsInstanceID()
