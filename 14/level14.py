#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/italy.html
"""

from PIL import Image, ImageDraw
from itertools import cycle

def generate_spiral(dim, cw, rotate):
  moves = {
      'down': lambda x,y: (x, y+1),
      'right': lambda x,y: (x+1, y),
      'up': lambda x,y: (x, y-1),
      'left': lambda x,y: (x-1, y)
      }

  x, y, traversed = 0, 0, set()

  def validate(dim, s):
    return lambda x,y:
      x >= 0 and x < dim \
        and y >= 0 and y < dim \
        and (x,y) not in s

  if cw:
    order = ['right', 'down', 'left', 'up']
  else:
    order = ['down', 'right', 'up', 'left']

  direction_iter = cycle(order)
  direction = direction_iter.next()
  while len(traversed) < dim*dim:
    traversed.add((x,y))
    yield x, y
    if not validate(*moves[direction](x, y)):
      direction = direction_iter.next()
    x, y = moves[direction](x,y)

im = Image.open('wire.png')
out = Image.new('RGB', (100,100))
draw = ImageDraw.Draw(out)

for num, pt in enumerate(generate_spiral(100, False)):
  draw.point(pt, fill=im.getpixel((num, 0)))

out.show()
del draw
