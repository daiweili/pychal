#!/usr/vin/env python

"""
http://repeat:switch@www.pythonchallenge.com/pc/ring/grandpa.html
"""

import requests
from StringIO import StringIO
from PIL import Image
from itertools import izip_longest

print 'The image is of Grandfather rock on Koh Samui island in Thailand'

r = requests.get('http://www.pythonchallenge.com/pc/rock/mandelbrot.gif', auth=('kohsamui', 'thailand'))
im = Image.open(StringIO(r.content))
w, h = im.size

def grouper(n, iterable, fillvalue=None):
  "Collect data into fixed-length chunks or blocks"
  # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
  args = [iter(iterable)] * n
  return izip_longest(fillvalue=fillvalue, *args)

palette = list(grouper(3, im.getpalette()))

out = Image.new('RGB', im.size)

MAX_ITER = 128
raw = []
data = []
for y in xrange(h):
  for x in xrange(w):
    x0 = 0.34 + (x/float(w) * 0.036)
    y0 = 0.57 + ((h-y-1)/float(h) * 0.027)
    c0 = complex(x0, y0)
    c = c0
    in_set = True
    for z in xrange(MAX_ITER):
      if abs(c) >= 2.0:
        raw.append(z)
        data.append(palette[z])
        in_set = False
        break
      c *= c
      c += c0
    if in_set:
      raw.append(MAX_ITER-1)
      data.append(palette[MAX_ITER-1])

diff = []
for i, pix in enumerate(im.getdata()):
  if raw[i] != pix:
    if raw[i] < pix:
      diff.append((0,0,0))
    else:
      diff.append((255,255,255))

out.putdata(data)
out.show()

out2 = Image.new('RGB', (23, 73))
out2.putdata(diff)
out2.show()

print 'The second picture is the Aceribo Message'

