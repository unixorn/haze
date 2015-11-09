# Copyright (c) 2015 Joe Block <jpb@unixorn.net>
#
# This code is released under the Apache 2.0 license
# See the LICENSE file in this repository for details

from haze.ec2 import myRegion

# Bash helpers
def cliMyRegion():
  """Print a running instance's instance ID"""
  print myRegion()

if __name__ == "__main__":
  cliMyRegion()
