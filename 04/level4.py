#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import urllib, urllib2
import re
import sys

pat = re.compile('\d*$')
#guess = 12345
#guess = 8022
# At some point, it prints 16044 followed by:
#    Yes. Divide by two and keep going.
if len(sys.argv) != 2:
    guess = 12345
else:
    guess = sys.argv[1]

for i in xrange(400):
    r = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % guess)
    text = r.read()
    guess = pat.search(text).group(0)
    print guess
    if not guess:
        print text
        break
