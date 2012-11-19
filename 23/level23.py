#!/usr/bin/env python

import string

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/bonus.html
"""

hint = "va gur snpr bs jung?"

shift = 13
lc = string.ascii_lowercase
trans = string.maketrans(lc, lc[shift:] + lc[:shift])
print string.translate(hint, trans)

# in the face of what?

# import this -> In the face of ambiguity
print
import this
print

print 'http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html'

