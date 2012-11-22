#!/usr/bin/env python

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/lake.html
"""

import requests
from StringIO import StringIO
from PIL import Image
import wave
from itertools import izip_longest, cycle, islice

im = Image.new('RGB', (300, 300))

# Recipes from http://docs.python.org/2/library/itertools.html#recipes
# Itertools is so awesome

def grouper(n, iterable, fillvalue=None):
  "Collect data into fixed-length chunks or blocks"
  # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
  args = [iter(iterable)] * n
  return izip_longest(fillvalue=fillvalue, *args)

def roundrobin(*iterables):
  "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
  # Recipe credited to George Sakkis
  pending = len(iterables)
  nexts = cycle(iter(it).next for it in iterables)
  while pending:
    try:
      for next in nexts:
        yield next()
    except StopIteration:
      pending -= 1
      nexts = cycle(islice(nexts, pending))

pixels = []
for n in xrange(5):
  data = []
  # Each wav file encodes 60x60 RGB pixels
  for num in xrange(1,6):
    r = requests.get('http://www.pythonchallenge.com/pc/hex/lake%d.wav' % (num + n*5), auth=('butter', 'fly'))
    w = wave.open(StringIO(r.content))
    l = w.readframes(w.getnframes())
    # Make lists of 60 RGB pixels
    cur = list(grouper(60, grouper(3, map(ord, l))))
    data.append(cur)
  # Grab 60 pixels at a time from each of 5 wav files (300 a row)
  for group in roundrobin(*data):
    pixels.extend(group)

im.putdata(pixels)
im.show()
