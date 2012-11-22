#!/usr/vin/env python

"""
http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.html
"""

import requests
from PIL import Image
from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
  "Collect data into fixed-length chunks or blocks"
  # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
  args = [iter(iterable)] * n
  return izip_longest(fillvalue=fillvalue, *args)

r = requests.get('http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv', auth=('repeat','switch'))
vals = map(lambda x: float(x.strip())*255, r.content.split(','))

im = Image.new('L', (53, 139))
im.putdata(vals)
im = im.rotate(-90)
im = im.transform(im.size, Image.EXTENT, (im.size[0], 0, 0, im.size[1]))
im.show()

vals = map(lambda x: x.strip(), r.content.split(','))

n = []
for x in grouper(3, vals, '0.000000'):
  n.append(str(x[0])[5] + str(x[1])[5] + str(x[2])[6])

print ''.join(map(lambda x: chr(int(x)), n))

