#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/5808.html
"""

from PIL import Image

im = Image.open('cave.jpg')

even = Image.new('RGB', map(lambda x: x/2, im.size), (255, 255, 255))
even_pixels = even.load()

for x in xrange(0, im.size[0], 2):
  for y in xrange(0, im.size[1], 2):
    even_pixels[x/2, y/2] = im.getpixel((x,y))

even.show()

odd = Image.new('RGB', im.size, (255, 255, 255))
odd_pixels = odd.load()

for x in xrange(1, im.size[0], 2):
  for y in xrange(1, im.size[1], 2):
    odd_pixels[int(x/2), int(y/2)] = im.getpixel((x,y))

odd.show()
