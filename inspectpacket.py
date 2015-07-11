#!/usr/bin/python
import sys, string

with open(sys.argv[1]) as f:
    lines = f.readlines()

line = string.split(lines[0].rstrip('\n'), ' ')[7]
hexs = [line[x:x+2] for x in xrange(0, len(line), 2)]

offs = [0, 16, 24, 1, 129, 55, 169, 87, 35, 70, 23, 0]

ints = [int(x, 16) for x in hexs]

k = ints[0]
print "k:", k
subs = [x-y for(x,y) in zip(ints, offs)]

i=0
while i < 12:
    if subs[i] < 0:
        subs[i]+=256
    i+=1

deobfs = [s^k for s in subs]
deobfs[0] = k
print deobfs[0:-1]

# checksum
j = 0
i = 0

while i <= 10:
    j += deobfs[i] & 0xff
    i += 1
checksum = ((( (k ^ j) & 0xff) + 131) & 0xff)

#print checksum
#print ints[11]
