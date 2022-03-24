---
title: "[cputime]"
description: "measure CPU time"
bref: "measure CPU time"
draft: false
categories: ["object"]
pd-category: "Time"
---

### [cputime]

Measure CPU time.

The cputime object measures elapsed CPU time,  as measured by your operating system. This appears to work on NT,  IRIX,  and Linux,  but not on W98.

INLET:

- 1st

  - bang - reset (set elapsed time to zero).
  
- 2nd
  
  - bang - time to measure.

OUTLET:

- bang - output elapsed time.

ARGUMENTS:

- NONE.



> see also [[realtime]](../realtime) [[timer]](../timer)
 
> updated for Pd version 0.33
