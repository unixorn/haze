# Copyright (c) 2015 Joe Block <jpb@unixorn.net>
#
# This code is released under the Apache 2.0 license
# See the LICENSE file in this repository for details
#
# I have often found it convenient to be able to read what instance ID an
# instance is from inside bash provisioning scripts.

from haze.ec2 import myInstanceID

# Bash helpers
def awsInstanceID():
  """Print a running instance's instance ID"""
  print myInstanceID()

if __name__ == "__main__":
  awsInstanceID()
