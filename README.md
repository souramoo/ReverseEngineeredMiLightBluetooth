# Reverse Engineered MiLight Bluetooth
Control a £20 bluetooth lightbulb from your linux computer/RPi for fun and profit!

## The Story
So I thought it would be cool to have wirelessly controlled lightbulbs in my room. Phillips Hue is /expensive/, especiallt for a poor student like me. Thanks to the magical realm of eBay, I found a cheap chinese unbranded(?) bluetooth-controlled lightbulb for £20. I bought it and installed it. After fiddling around with E27 to bayonet adapters, it was connected!

Now, to control it! I download the android app, and it... kinda works? It manages to crash the bluetooth stack of the phone so badly that I need to adb into it to ``killall com.android.bluetooth``. Well, so it kinda worked but the app is pretty rubbish. And they have no API.

And although the bulb said "MiLight" on the packaging, the MiLight website makes no reference to any bluetooth controlled bulbs. What am I to do?

## The Solution
I used the bluetooth packet logger in android 4.4+ to log bluetooth packets sent/received while using the app. I performed a simple packet replay using gatttool. By obtaining various payloads, I was able to control it from the computer!

I still had no idea what the packet protocol was at this point. You can do this for your own unidentified bulb using the same techniques I used, described in ``how_to_collect_commands``

You can see the commands I collected at this stage in the ``commands/`` folder.

### Investigating the protocol
I disassembled the apk and looked through the functions that sent data over Bluetooth (LE, only in 4.0+) and reconstructed the batshit crazy obfuscation algorithm both in forward (``createpacket.py``) and in reverse (``inspectpacket.py``) to investigate the actual protocol structure.

It appears that the first byte is a RANDOM NUMBER that is used as a key. The next ten bytes appear to be used as the payload, xor'd with the key and with various constants added on for some reason. Then there is a calculated checksum in the 12th byte.

I detail what I gather about the protocol in protocol_info and feel free to use inspectpacket.py <command file name> to look at what is going on in the commands present in the commands folder (or adapt it to your own needs) and to generate your own commands using ``createpacket.py``

### Assembling useful functionality
After even more fiddling about I have assembled useful functionality to change the lightbulb color and brightness in change\_color.sh and to change the "temperature" (yellowy white LED) and brightness in change\_temp.sh. I also assemble the turn on script in ``on.sh`` and turn off light script in ``off.sh``

### USAGE
To use this, you will need to first identify the MAC address of your bulb:
```
hcitool lescan
```
And copy this MAC address somewhere. Then, you will need to extract two numbers calculated from your MAC address. You will probably need to fetch some packets off your phone app communicating with the light and find the ones with attr 0x0012 after opening the capture file in wireshark. Get the hex stream payload and put it in a file similar to a .command file in ``commands/`` - after running ``inspectpacket.py``, you will get something like:

```
[ (random number), 161, (first number), (second number), ... ]
```

You should get two numbers, each on a separate line. Next, insert these numbers into all of the files.

```
find . -name "*" -exec sed -ri 's/\$BULB_ID1/(first number here)/g' {} ';'
find . -name "*" -exec sed -ri 's/\$BULB_ID2/(second number here)/g' {} ';'
find . -name "*" -exec sed -ri 's/\$BULB_MAC/(bulb mac address here)/g' {} ';'
```

For example,
```
find . -name "*" -exec sed -ri 's/\$BULB_ID1/1/g' {} ';'
find . -name "*" -exec sed -ri 's/\$BULB_ID2/2/g' {} ';'
find . -name "*" -exec sed -ri 's/\$BULB_MAC/00:11:22:33:44:55/g' {} ';'
```

Now, you should be able to turn your light on:

```
./on.sh
```

And change colours:

```
./change_color.sh 60 100
```

And change the brightness on the same color:
```
./change_color.sh 60 10
```

And change it to white:
```
./change_temp.sh 140 100
```

And dim the white LED:
```
./change_temp.sh 140 10
```

And turn it yellowy:
```
./change_temp.sh 1 100
```

## The end
I have also integrated this into my home automation system based on my raspberry pi so that I can control the lightbulb over wifi rather than bluetooth. Who needs silly dedicated wifi bridges anyway?
