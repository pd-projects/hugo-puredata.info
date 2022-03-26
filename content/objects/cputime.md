---
title: cputime
description: measure CPU time
categories:
- object
last_update: '0.33'
see_also:
- realtime
- timer
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
The cputime object measures elapsed CPU time,  as measured by your operating system. This appears to work on NT,  IRIX,  and Linux,  but not on W98.
