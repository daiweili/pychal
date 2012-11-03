#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/bull.html
"""

def say_it(num):
  count = 1
  prev = None
  out = ''
  for c in num:
    if c != prev:
      if prev != None:
        out += '%d%s' % (count, prev)
      prev = c
      count = 1
    else:
      count += 1
  out += '%d%s' % (count, prev)
  return out

num = '1'
for i in xrange(30):
  num = say_it(num)

print "http://huge:file@www.pythonchallenge.com/pc/return/%d.html" % len(num)

