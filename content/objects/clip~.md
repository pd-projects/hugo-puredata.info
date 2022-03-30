---
title: clip~
description: restrict a signal between two limits
categories:
- object
last_update: "0.33"
see_also:
- min~
- max~
- clip
- expr~
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

arguments:
  1) float: initial lower limit (default 0).
  2) float: initial upper limit (default 0).
draft: false
pdcategory: Audio Math

---

The clip~ object passes its signal input to its output, clipping it to lie between two limits.
