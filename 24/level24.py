#!/usr/bin/env python

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html
"""

import requests
from StringIO import StringIO
from PIL import Image, ImageDraw
from search import AStarSearch
import numpy as np

r = requests.get('http://www.pythonchallenge.com/pc/hex/maze.png', auth=('butter', 'fly'))
im = Image.open(StringIO(r.content))
pix = im.load()

start = (639, 0)
goal = (1, 640)

w, h = im.size

def ispath(pix):
  r,g,b,a = pix
  return not (r > 0 and g > 0 and b > 0)

grid = np.zeros((w,h))
for y in xrange(h):
  for x in xrange(w):
    if ispath(pix[x,y]):
      grid[x,y] = 1

path = AStarSearch(start, goal, grid)

bytes = ''
for num, pos in enumerate(path):
  r,g,b,a = pix[pos]
  if num % 2 == 1:
    bytes += chr(r)

out = Image.new('RGB', im.size, 0)
draw = ImageDraw.Draw(out)
draw.line(path, fill=(255,255,255))
del draw
out.show()

with open('out','w') as f:
  f.write(bytes)

