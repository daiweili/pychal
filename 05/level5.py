#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/def/peak.html
"""

import pickle

obj = pickle.load(open('banner.p', 'r'))
# One-liner
print '\n'.join([''.join([c*n for c,n in l]) for l in obj])
# Original
#for list in obj:
#    line = []
#    for o in list:
#        line += o[0] * o[1]
#    print ''.join(line)
