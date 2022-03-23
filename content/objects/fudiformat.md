---
title: "[fudiformat]"
description: ""
bref: ""
draft: false
categories: ["object", "I/O via MIDI, OSC, and FUDI"]
---

### [fudiformat]

FUDI stands for "Fast Universal Digital Interface" and is a networking protocol used by Pd. The fudiformat object makes FUDI messages suitable for sending over the network via netsend (in UDP mode). Incoming messages are output as FUDI messages, byte by byte. The '-u' creation argument switches to "UDP" mode, omitting the packet separator. This saves some two bytes, but only works when sending single FUDI messages over UDP. It doesn't work with TCP/IP (however, you can use the default format even with UDP transport).

INLET:

- anything - any message to convert to a FUDI packet.

OUTLET:

- list - converted FUDI packet.

FLAG:

- '-u': switches to "UDP" mode

> see also [[fudiparse]](../fudiparse) [[oscformat]](../oscformat) 

> updated for Pd version 0.48
 
