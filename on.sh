#!/bin/bash

gatttool -b $BULB_MAC --char-write-req -a 0x0012 -n `./createpacket.py "[32, 161, $BULB_ID1, $BULB_ID2, 2, 1, 0, 0, 0, 0, 0]"`
