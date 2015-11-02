#!/usr/bin/env python2
import sys

name = sys.argv[1]
num = int(name[1:3], 16) & 0xff
num = num << 8
num = num | (int(name[3:5], 16) & 0xff)

print "BULB_ID1=%d" % (num >> 8)
print "BULB_ID2=%d" % (num % 256)
