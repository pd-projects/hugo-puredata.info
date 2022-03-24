---
title: "[bendout]"
description: ""
bref: ""
draft: false
categories: ["object"]
pd-category: "I/O via MIDI, OSC, and FUDI"
---

### [bendout]

**Known bug:** [bendin] and [bendout] are inconsistent ([bendin] outputs values from 0 to 16383 and [bendout] takes values from -8192 to 8191) - this won't change.

INLETS:

- 1st: 
 
  - float - MIDI bend value.
  
- 2nd: 

  - float - MIDI channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- float - MIDI channel/port


> see also [[notein]](../notein) (etc) - MIDI in objects.

> see also [[noteout]](../noteout) (etc) - MIDI out objects.

> updated for Pd version 0.48-2
 
