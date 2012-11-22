#!/usr/vin/env python

"""
http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html
"""

import requests
import re
import bz2

pat = re.compile('</html>\s(.*)', re.M | re.S)
r = requests.get('http://www.pythonchallenge.com/pc/ring/guido.html', auth=('repeat','switch'))
cont = pat.search(r.content).group(1)
lines = cont.split('\n')

out = bz2.decompress(''.join([chr(len(line)) for line in lines]))
print out
