#!/bin/bash

gatttool -b $BULB_MAC --char-write-req -a 0x0012 -n `./createpacket.py "[85, 161, $BULB_ID1, $BULB_ID2, 2, 2, 0, 0, 0, 0, 0]"`
