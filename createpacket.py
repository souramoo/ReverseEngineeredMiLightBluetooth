#!/usr/bin/env python2
import sys, string

data = sys.argv[1]
input = eval(data)

k = input[0]

# checksum
j = 0
i = 0

while i <= 10:
    j += input[i] & 0xff
    i += 1
checksum = ((( (k ^ j) & 0xff) + 131) & 0xff)

xored = [(s&0xff)^k for s in input]

offs = [0, 16, 24, 1, 129, 55, 169, 87, 35, 70, 23, 0]

adds = [x+y&0xff for(x,y) in zip(xored, offs)]

adds[0] = k
adds.append(checksum)
#print checksum

hexs = [hex(x) for x in adds]
hexs = [x[2:] for x in hexs]
hexs = [x.zfill(2) for x in hexs]

print ''.join(hexs)
