---
title: clip
description: force a number into a range
bref: force a number into a range
categories:
- object
last_update: '0.47'
see_also:
- clip~
- expr
- max
- min
arguments:
  1st float: initial lower limit (default 0).
  2nd float: initial upper limit (default 0).
inlets:
  1st:
    bang: re clip last incomming number between the two limits.
    float: number to clip.
  2nd:
    float: set lower limit.
  3rd:
    float: set upper limit.
outlets:
  1st:
    float: the clipped value.
draft: false
pdcategory: Math

---
Bound a number between two limits.

The clip object passes its signal input to its output,  clipping it to lie between two limits.
