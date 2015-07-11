It appears that the data is sent as an obfuscated 12 byte stream.

The first byte is a random number used as a key for deobfuscation.
There is a weird algorithm I have extracted and implemented into create_packet.py and inspect_packet.py.
The last byte is a checksum and is excluded from the output of these scripts and is calculated on the fly.

So, once decoded, the first byte passed to create_packet can be any number of your choosing.
The next few parameters are somewhat mysterious, but the second byte appears to be 161, and the third and fourth are related to the id of the bulb itself.
There is an action byte and a parameter byte.
The last three bytes appear to be 0.

Hope this helps in decoding messages sent to the bulb.
