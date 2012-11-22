#!/usr/bin/env python

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/decent.html
"""

import hashlib
import sys

lst = []

with open('mybroken.zip', 'rb') as f:
  l = f.read()
  for i in xrange(len(l)):
    tmp = ord(l[i])
    lst = list(l)
    for b in xrange(255):
      lst[i] = chr(b)
      m = hashlib.md5()
      m.update(''.join(lst))
      if m.hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
        print m.hexdigest()
        print 'Changed %x to %x at index %d' % (tmp, b, i)
        with open('fixed.zip', 'w') as f:
          f.write(''.join(lst))
          sys.exit(0)

print 'Output at fixed.zip'
print
print 'You\'re missing the boat -> speed + boat'
print 'http://butter:fly@www.pythonchallenge.com/pc/hex/speedboat.html'
