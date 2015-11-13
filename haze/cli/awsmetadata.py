# Copyright (c) 2015 Joe Block <jpb@unixorn.net>
#
# This code is released under the Apache 2.0 license
# See the LICENSE file in this repository for details
#
# I have often found it convenient to be able to read what AWS region
# an instance is in inside bash scripts.

import argparse
from haze.ec2 import getMetadataKey

# Bash helpers
def awsReadMetadataKey():
  """Print key from a running instance's metadata"""
  parser = argparse.ArgumentParser()

  parser.add_argument("--key",
                      dest="keyname",
                      required=True,
                      help="Which metadata key to read")

  cli = parser.parse_args()

  print getMetadataKey(name=cli.keyname)

if __name__ == "__main__":
  awsReadMetadataKey()
