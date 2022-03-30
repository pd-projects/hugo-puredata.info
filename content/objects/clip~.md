---
title: clip~
description: restrict a signal between two limits
categories:
- object
pdcategory: Audio Math
last_update: '0.33'
see_also:
- min~
- max~
- clip
- expr~
arguments:
- type: 1) float
  description: initial lower limit (default 0).
- type: 2) float
  description: initial upper limit (default 0).
inlets:
  1st:
    signal: signal value to clip.
  2nd:
    float: set lower limit.
  3rd:
    float: set upper limit.
outlets:
  1st:
    signal: the clipped signal.
draft: false
---
The clip~ object passes its signal input to its output, clipping it to lie between two limits.
