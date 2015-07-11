#!/bin/bash

## Usage: ./change_color color(0-255) brightness(0-100)

gatttool -b $BULB_MAC --char-write-req -a 0x0012 -n `./createpacket.py "[45, 161, $BULB_ID1, $BULB_ID2, 2, 4, $1, 100, 0, 0, 0]"`
gatttool -b $BULB_MAC --char-write-req -a 0x0012 -n `./createpacket.py "[45, 161, $BULB_ID1, $BULB_ID2, 2, 5, $1, $2, 0, 0, 0]"`
