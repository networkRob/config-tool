#!/usr/bin/env python3
#
# Copyright (c) 2020, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#  - Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#  - Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#  - Neither the name of Arista Networks nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# config-tool.py -- this is a very generic name, it may change
#
#    Written by:
#       Corey Hines, Arista Networks
#
"""
DESCRIPTION
an attempt to recover EOS configuration stanzas that are common amongst a corpus of configs
"""

import pathlib
import collections
# to be used in the next revision
import re

from os.path import expanduser
home = expanduser("~")

mydir = home + "/vs-code/config-tool/configs/"


def get_dupes(L):
    seen = set()
    seen2 = set()
    seen_add = seen.add
    seen2_add = seen2.add
    for item in L:
        if item in seen:
          seen2_add(item)
        else:
          seen_add(item)
    return list(seen2)


stanzas = []
comments = []
for path in pathlib.Path(mydir).iterdir():
    if path.is_file():
        current_file = open(path, "r")
        content = current_file.read()
        # this is broken, need to import re and filter comments another way
        comments += content.split('!!')
        stanzas += content.split('!')
        current_file.close()

## these print statements are for debugging/testing
print(len(stanzas))
print(len(comments))
dupes = get_dupes(stanzas)
#print(len(dupes))

# printing is ok for now but should save to a file or ask.
# it is also nice to just redirect the output to a file user's choice
print("\n".join(dupes))

# once the comments gathering code is fixed, this should be useful
#print("##################### COMMENTS #######################")
#print("\n".join(comments))
