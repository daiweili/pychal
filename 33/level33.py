#!/usr/bin/env python

"""
http://kohsamui:island@www.pythonchallenge.com/pc/rock/beer.html
"""

from PIL import Image
import requests
from StringIO import StringIO
from collections import Counter
from math import sqrt

r = requests.get('http://www.pythonchallenge.com/pc/rock/beer2.png', auth=('kohsamui', 'thailand'))

def is_square(x):
    return sqrt(x) == int(sqrt(x))

im = Image.open(StringIO(r.content))
w, h = im.size

data = im.getdata()
pix = Counter(im.getdata())

total = 0
cnt = 0
for value, count in reversed(sorted(pix.iteritems())):
    max_pix = value
    total += count
    if w*h - total <= 0:
        break
    if is_square(w*h - total):
        data = filter(lambda x: x < max_pix, data)
        pix = Counter(data)
        dim = int(sqrt(w*h - total))
        out = Image.new('L', (dim, dim))
        max_data = max(data)
        out.putdata(map(lambda pix: int(pix * 255.0 / max_data), data))
        if dim < 112:
            # out.show()
            out.save('image%02d.png' % cnt)
            cnt += 1
        del out

print 'The letters gremlins are boxed'
