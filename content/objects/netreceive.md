---
title: netreceive
description: listen for incoming messages from network
categories:
- object
pdcategory: Misc
last_update: '0.51'
see_also:
- netsend
arguments:
- type: float
  description: port number
- type: symbol
  description: UDP hostname or multicast address.
flags:
- flag: -u
  description: sets UDP connection (default TCP).
- flag: -b
  description: sets to binary mode (default 'FUDI').
- flag: -f
  description: flag for from address & port outlet.
inlets:
  1st:
    list: works like 'send'.
    listen <float, symbol>: a number sets or changes the port number (0 or negative
      closes the port). Optional symbol is a hostname which can be a UDP multicast
      address or a network interface.
    send <anything>: sends messages back to connected netsend objects.
outlets:
  1st:
    anything: messages sent from connected netsend objects.
  2nd:
    float: number of open connections for TCP connections. (TCP connection only)
  rightmost:
    list: address and port. (if the -f flag is given)
draft: false
---
As of 0.51, Pd supports IPv6 addresses.

The netreceive object opens a socket for TCP ("stream") or UDP ("datagram") network reception on a specified port. If using TCP, an outlet gives you the number of netsend objects (or other compatible clients) that have opened connections here.

By default the messages are ASCII text messages compatible with Pd (i.e., numbers and symbols terminated with a semicolon -- the "FUDI" protocol). The "-b" creation argument specifies binary messages instead, which appear in Pd as lists of numbers from 0 to 255 (You could use this for OSC messages, for example.)

There are some possibilities for intercommunication with other programs... see the help for "netsend."

SECURITY NOTE: Don't publish the port number of your netreceive unless you wouldn't mind other people being able to send you messages.

An old (pre-0.45) calling convention is provided for compatibility, port number and following "0" or "1" for TCP or UDP respectively.
