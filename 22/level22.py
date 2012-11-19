#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/hex/copper.html
"""

import requests
from StringIO import StringIO
from PIL import Image, ImageDraw
import pdb

r = requests.get('http://www.pythonchallenge.com/pc/hex/white.gif', auth=('butter','fly'))
im = Image.open(StringIO(r.content))

w, h = im.size

def getpt(im):
  for x in xrange(w):
    for y in xrange(h):
      if im.getpixel((x,y)) != 0:
        return (x,y)

pts = []
frame = 0

while True:
  try:
    # Get non-black pixels from current frame
    pts.append(getpt(im))
    frame += 1
    # Advance a frame
    im.seek(im.tell()+1)
  except:
    break

base_x = 100
cur = (base_x, 100)
line = [base_x,100]

out = Image.new('RGB', (1200, 200), 0)
d = ImageDraw.Draw(out)

for pt in pts:
  x,y = pt
  if x == 100 and y == 100:
    line += cur
    d.line(line, fill=255)
    print line
    base_x += 200
    line = [base_x, 100]
    cur = (base_x, 100)
    continue
  line += cur
  cur_x, cur_y = cur
  cur = (cur_x + (x - 100)*3, cur_y + (y - 100)*3)

if line:
  d.line(line, fill=255)

out.show()



