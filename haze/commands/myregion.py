# Copyright (c) 2015 Joe Block <jpb@unixorn.net>
#
# This code is released under the Apache 2.0 license
# See the LICENSE file in this repository for details
#
# I have often found it convenient to be able to read what AWS region
# an instance is in inside bash scripts.

from haze.ec2 import myRegion

# Bash helpers
def awsMyRegion():
  """Print a running instance's instance ID"""
  print myRegion()

if __name__ == "__main__":
  awsMyRegion()
