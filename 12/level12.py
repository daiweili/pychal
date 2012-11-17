#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/evil.html
"""

"""
evil4.jpg says Bert is evil! go back!
"""
imgs = []
for i in xrange(5):
  imgs.append(open('img%d.out' % i, 'w'))

[imgs[i % 5].write(byte) for i, byte in enumerate(open('evil2.gfx', 'rb').read())]
