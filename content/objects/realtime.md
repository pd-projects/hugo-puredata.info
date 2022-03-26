---
title: realtime
description: measure real time
bref: measure real time
categories:
- object
last_update: '0.33'
see_also:
- timer
- cputime
inlets:
  1st:
    bang: reset (set elapsed time to zero).
  2nd:
    bang: time to measure.
outlets:
  1st:
    bang: output elapsed time.
draft: false
pdcategory: Time

---
Ask OS for elapsed real time.

The realtime object measures elapsed real time,  as measured by your operating system.
