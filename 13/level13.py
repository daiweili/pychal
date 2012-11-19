#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
"""

from xmlrpclib import ServerProxy, Error

server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

# print server.system.listMethods()
print server.phone('Bert')
