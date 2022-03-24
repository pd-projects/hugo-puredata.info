---
title: "[pgmin]"
description: ""
bref: ""
draft: false
categories: ["object"]
pd-category: "I/O via MIDI, OSC, and FUDI"
---

### [pgmin]

**Known bug:** Program change values in [pgmin] and [pgmout] are indexed from 1, which means that the possible values are from 1 to 128 (not 0 to 127)!

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI program value.
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- float - MIDI channel/port

> see also [[notein]](../notein) (etc) - MIDI in objects.

> see also [[noteout]](../noteout) (etc) - MIDI out objects.

> updated for Pd version 0.48-2
 
