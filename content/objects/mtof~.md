---
title: mtof~
description: acoustic conversions for audio signals
categories:
- object
see_also:
- mtof
- expr~
pdcategory: Audio Math
last_update: '0.33'
inlets:
  1st:
  - type: signal
    description: incoming value to be converted.
outlets:
  1st:
  - type: signal
    description: converted value.
draft: false
---
These objects convert MIDI pitch to frequency and back, and dB to and from RMS and power. They take audio signals as input and output (and work sample by sample.) Since they call library math functions, they may be much more expensive than other workaday tilde objects such as *~ and osc~, depending on your hardware and math library.

Boundary conditions are handled "reasonably". 100 db is assigned an RMS of 1, and dbtorms~ and dbtopow~ output true zero for 0 dB and less.