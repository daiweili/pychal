#!/usr/vin/env python

"""
http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
"""

import calendar

for year in xrange(6, 2007, 10):
  if calendar.isleap(year) \
    and calendar.weekday(year, 1, 1) == calendar.THURSDAY \
    and str(year)[0] == '1':
    print year

# Second youngest -> 1756
# January 27, 1756 -> Mozart's birthday
print 'http://huge:file@www.pythonchallenge.com/pc/return/mozart.html'
