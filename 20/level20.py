#!/usr/vin/env python

"""
http://www.pythonchallenge.com/pc/hex/idiot2.html
"""

import requests
from StringIO import StringIO
import re

b = (30203, 30204)
headers = {'Range':'bytes=%d-%d' % b}

pat = re.compile('bytes (\d+)-(\d+)')

while True:
  r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=('butter','fly'), headers=headers)
  print r.content
  if r.headers['content-range']:
    res = pat.match(r.headers['content-range'])
    b = (int(res.group(2))+1, int(res.group(2))+2)
    headers = {'Range':'bytes=%d-%d' % b}
  else:
    break

b = (2123456788, 2123456789)
headers = {'Range':'bytes=%d-%d' % b}

r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=('butter','fly'), headers=headers)
print r.content

b = (1152983631, 1152983632)
headers = {'Range':'bytes=%d-%d' % b}

r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=('butter','fly'), headers=headers)

"""
level 21
"""
import struct
import zlib
import bz2
import sys
import zipfile

def isbz2(s):
  return s.startswith('BZh91AY')

# 0x789c
def iszlib(s):
  return ord(s[0]) == 120 and ord(s[1]) == 156

def decompressible(f, r):
  return isbz2(f) or iszlib(f) or isbz2(r) or iszlib(r)

def reverse(s):
  return struct.pack('%dB' % len(s), *struct.unpack('%dB' % len(s), s)[::-1])

z = zipfile.ZipFile(StringIO(r.content))
pwd = 'invader'[::-1]
f = z.open('package.pack', 'r', pwd)

fwd = zlib.decompress(f.read())
rev = reverse(fwd)

while decompressible(fwd, rev):
  if iszlib(fwd):
    sys.stdout.write(' ')
    fwd = zlib.decompress(fwd)
  elif isbz2(fwd):
    sys.stdout.write('*')
    fwd = bz2.decompress(fwd)
  elif iszlib(rev):
    sys.stdout.write('\n')
    fwd = zlib.decompress(rev)
  elif isbz2(rev):
    sys.stdout.write('\n')
    fwd = bz2.decompress(rev)
  rev = reverse(fwd)

sys.stdout.write('\n')

print fwd[::-1]

