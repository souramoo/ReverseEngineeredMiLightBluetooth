1. Turn on Bluetooth HCI Snooping in Developer Settings
2. Open app and connect to light
3. Pull log via adb (e.g. a.log)
4. Turn light on
5. Pull log to a different filename (e.g. b.log)
6. Open a.log in wireshark and remember the packet number of the last packet.
7. Open b.log in wireshark and FOR EACH of the packets sent from localhost after the last packet in a.log:
    Run gatttool -b <MAC ADDRESS> --char-write-req -a <ATTRIBUTE NUMBER FROM PACKET> -n <HEX STREAM VALUE OF PAKCET>
Until the light does what you want.
8. Repeat for all the features you wish to elucidate.
