#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/5808.html
"""

from PIL import Image

im = Image.open('cave.jpg')

even = Image.new('RGB', map(lambda x: x/2, im.size))
odd = Image.new('RGB', map(lambda x: x/2, im.size))

odd_pixels = odd.load()
even_pixels = even.load()

for x in xrange(im.size[0]):
  for y in xrange(im.size[1]):
    if not(x & 1) and not(y & 1):
      even_pixels[x/2, y/2] = im.getpixel((x,y))
    elif x & 1 and y & 1:
      odd_pixels[int(x/2), int(y/2)] = im.getpixel((x,y))

even.show()
odd.show()
