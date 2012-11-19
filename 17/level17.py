#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/romance.html
"""

import requests
import re
import sys
import bz2
import urllib

pat = re.compile('\d*$')

if len(sys.argv) != 2:
  guess = 12345
else:
  guess = sys.argv[1]

result = ''
for i in xrange(400):
  r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s' % guess)
  result += r.cookies['info']
  guess = pat.search(r.text).group(0)
  if not guess:
    print r.text
    break

# result looks like:
# BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
# have to unquote
print bz2.decompress(urllib.unquote_plus(result))
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
# Mozart's father = Leopold -> look up his phone number

from xmlrpclib import ServerProxy
server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('Leopold')
# 555-VIOLIN

cookies = dict(info='the flowers are on their way')
r = requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php', cookies=cookies)
print r.content
# oh well, don't you dare to forget the balloons

print 'http://huge:file@www.pythonchallenge.com/pc/return/balloons.html'
