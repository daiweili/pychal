#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
"""

from PIL import Image, ImageDraw

im = Image.open('mozart.gif')
image = im.load()
out = Image.new('RGB', im.size)
draw = ImageDraw.Draw(out)

w, h = im.size
last = image[0,0]

for y in xrange(h):
  for x in xrange(w):
    if image[x,y] == 195:
      for x2 in xrange(x, w):
        draw.point((x2-x, y), fill=image[x2,y])
      for x2 in xrange(0, x):
        draw.point((x2+x, y), fill=image[x2,y])
      break

out.show()
del draw
