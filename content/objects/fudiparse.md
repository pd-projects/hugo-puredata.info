---
title: "[fudiparse]"
description: "FUDI messages to and from Pd lists"
bref: "FUDI messages to and from Pd lists"
draft: false
categories: ["object"]
pdcategory: "I/O via MIDI, OSC, and FUDI"
---

### [fudiparse]

The fudiparse object takes incoming lists of numbers, interpreting them as the bytes in a FUDI message (as received when sending Pd-messages via [netreceive -b]).

INLET:

- list - FUDI packet to convert to Pd messages.

OUTLET:

- anything - Pd messages.

ARGUMENTS:

- NONE.

> see also [[fudiformat]](../fudiformat) [[oscformat]](../oscformat) 

> updated for Pd version 0.48
 
