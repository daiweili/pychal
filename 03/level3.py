#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/def/equality.html
"""

"""
Hint: One small letter, surrounded by EXACTLY three big bodyguards on
each of its sides. (text in equality.txt)
"""

# Woops, should've just used re
#import string
#from collections import deque
#
#buf = deque()
#bufcase = deque()
#ans = []
#
#with open('equality.txt','r') as f:
#    for c in f.read():
#        if c in string.ascii_letters:
#            if len(buf) == 9:
#                if sum(bufcase) == 6 and bufcase[4] == 0 and bufcase[0] == 0 and bufcase[-1] == 0:
#                    ans += buf[4]
#                buf.popleft()
#                bufcase.popleft()
#            buf.append(c)
#            bufcase.append(1 if c in string.ascii_uppercase else 0)

import re
pat = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

with open('equality.txt','r') as f:
    txt = f.read()

print 'http://www.pythonchallenge.com/pc/def/%s.html' % ''.join(pat.findall(txt))
