#!/usr/vin/env python

"""
http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.html
"""


import requests
from StringIO import StringIO
from PIL import Image
import sys
from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
  "Collect data into fixed-length chunks or blocks"
  # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
  args = [iter(iterable)] * n
  return izip_longest(fillvalue=fillvalue, *args)


r = requests.get('http://www.pythonchallenge.com/pc/ring/bell.png', auth=('repeat','switch'))
im = Image.open(StringIO(r.content))

for idx, pix in enumerate(grouper(2, im.getdata())):
  pix0, pix1 = pix
  diff = abs(pix1[1] - pix0[1])
  if diff != 42:
    sys.stdout.write(chr(diff))

print 'Guido van Rossum'
