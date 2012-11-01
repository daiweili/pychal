#!/usr/bin/env python

import string

"""
http://www.pythonchallenge.com/pc/def/map.html
"""

hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

trans = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print string.translate(hint, trans)

print "http://www.pythonchallenge.com/pc/def/%s.html" % string.translate('map', trans)
