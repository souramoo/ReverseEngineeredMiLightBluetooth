#!/bin/bash

## Usage: ./change_temp color(0-255) brightness(0-100)

gatttool -b $BULB_MAC --char-write-req -a 0x0012 -n `./createpacket.py "[20, 161, $BULB_ID1, $BULB_ID2, 4, 4, $1, 255, 0, 0, 0]"`
gatttool -b $BULB_MAC --char-write-req -a 0x0012 -n `./createpacket.py "[20, 161, $BULB_ID1, $BULB_ID2, 4, 5, $1, $2, 0, 0, 0]"`
