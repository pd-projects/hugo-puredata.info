---
title: "[fudiformat] [fudiparse]"
description: ""
bref: ""
draft: false
categories: ["object", "I/O via MIDI, OSC, and FUDI"]
---

### [fudiformat] [fudiparse]

FUDI stands for "Fast Universal Digital Interface" and is a networking protocol used by Pd. The fudiformat object makes FUDI messages suitable for sending over the network via netsend (in UDP mode). Incoming messages are output as FUDI messages, byte by byte. The '-u' creation argument switches to "UDP" mode, omitting the packet separator. This saves some two bytes, but only works when sending single FUDI messages over UDP. It doesn't work with TCP/IP (however, you can use the default format even with UDP transport).

---------------------


### [fudiformat]

INLET:

- anything - any message to convert to a FUDI packet.

OUTLET:

- list - converted FUDI packet.

FLAG:

- '-u': switches to "UDP" mode

---------------------

### [fudiparse]

The fudiparse object takes incoming lists of numbers, interpreting them as the bytes in a FUDI message (as received when sending Pd-messages via [netreceive -b]).

INLET:

- list - FUDI packet to convert to Pd messages.

OUTLET:

- anything - Pd messages.

ARGUMENTS:

- NONE.
 
 
> see also [[oscformat]](../osc-format-parse) 

> updated for Pd version 0.48