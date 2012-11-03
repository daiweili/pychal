#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""

from PIL import Image
import sys

im = Image.open('oxygen.png')

# Characters are 7 pixels apart apparently
prev = 0
for x in xrange(0, im.size[0], 7):
  pix = im.getpixel((x,50))
  r,g,b,a = pix
  if r==g==b:
    sys.stdout.write(chr(r))
print

# Above prints the following
#   smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
#   smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]

l = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print 'http://www.pythonchallenge.com/pc/def/%s.html' % ''.join(map(chr, l))
