---
title: fudiformat
categories:
- object
last_update: '0.48'
see_also:
- fudiparse
- oscformat
inlets:
  1st:
    anything: any message to convert to a FUDI packet.
outlets:
  1st:
    list: converted FUDI packet.
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
FUDI stands for "Fast Universal Digital Interface" and is a networking protocol used by Pd. The fudiformat object makes FUDI messages suitable for sending over the network via netsend (in UDP mode). Incoming messages are output as FUDI messages, byte by byte. The '-u' creation argument switches to "UDP" mode, omitting the packet separator. This saves some two bytes, but only works when sending single FUDI messages over UDP. It doesn't work with TCP/IP (however, you can use the default format even with UDP transport).

FLAG:

- '-u': switches to "UDP" mode
