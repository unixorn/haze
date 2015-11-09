# Copyright (c) 2015 Joe Block <jpb@unixorn.net>
#
# This code is released under the Apache 2.0 license
# See the LICENSE file in this repository for details

from haze.ec2 import myInstanceID

# Bash helpers
def cliInstanceID():
  """Print a running instance's instance ID"""
  print myInstanceID()

if __name__ == "__main__":
  cliInstanceID()
