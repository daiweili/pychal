#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""

"""
Hint: find rare characters in the mess below (mess in ocr.txt)
"""

from collections import Counter

counts = Counter()
letters = []

with open('ocr.txt','r') as f:
    for c in f.read():
        counts[c] += 1
        if c not in letters:
            letters += c

rare = [k for k,v in dict(counts).iteritems() if v==1]
letters = [c for c in letters if c in rare]
print 'http://www.pythonchallenge.com/pc/def/%s.html' % ''.join(letters)
