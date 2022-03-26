---
title: fudiparse
description: FUDI messages to and from Pd lists
categories:
- object
last_update: '0.48'
see_also:
- fudiformat
- oscformat
inlets:
  1st:
    list: FUDI packet to convert to Pd messages.
outlets:
  1st:
    anything: Pd messages.
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
The fudiparse object takes incoming lists of numbers, interpreting them as the bytes in a FUDI message (as received when sending Pd-messages via [netreceive -b]).
