#!/usr/bin/env python
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

"""
I have often found it convenient to be able to read arbitrary AWS metadata
for an instance inside bash scripts running on the instance.
"""

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
