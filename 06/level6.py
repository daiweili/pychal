#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

import sys
import re
from zipfile import *

pat = re.compile('\d*$')

if len(sys.argv) != 2:
    guess = 90052
else:
    guess = sys.argv[1]

f = ZipFile(open('channel.zip','r'))
print f.comment

while True:
    r = f.open('%s.txt' % guess)
    info = f.getinfo('%s.txt' % guess)
    text = r.read()
    guess = pat.search(text).group(0)
    sys.stdout.write(info.comment)
    if not guess:
        print text
        break
