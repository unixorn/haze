#!/usr/bin/env python
# Copyright (c) 2015 Joe Block <jpb@unixorn.net>
#
# This code is released under the Apache 2.0 license
# See the LICENSE file in this repository for details
#
# I have often found it convenient to be able to read what instance ID an
# instance is from inside bash provisioning scripts.

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
