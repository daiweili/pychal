#!/usr/vin/env python

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
"""

import base64
import re
import struct
import wave
import requests
from StringIO import StringIO

pat = re.compile('.*base64\s*(.*)--=======', flags = re.M | re.DOTALL)
r = requests.get('http://www.pythonchallenge.com/pc/hex/bin.html', auth=('butter','fly'))

orig = base64.b64decode(re.sub('\s+', '', pat.search(r.content).group(1)))

w = wave.open(StringIO(orig), 'rb')

sound = w.readframes(w.getnframes())
words = len(sound)/4
revsound = struct.pack('>%dl' % words, *struct.unpack('<%dl' % words, sound))

out = wave.open('out.wav', 'wb')
out.setparams(w.getparams())
out.writeframes(revsound)

w.close()
out.close()

print 'vlc out.wav'
print 'It should say "You are an idiot... hahahahahahha"'
