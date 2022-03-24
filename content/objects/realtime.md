---
title: "[realtime]"
description: "measure real time"
bref: "measure real time"
draft: false
categories: ["object"]
pd-category: "Time"
---

### [realtime]

Ask OS for elapsed real time.

The realtime object measures elapsed real time,  as measured by your operating system.

INLET:

- 1st

  - bang - reset (set elapsed time to zero).

- 2nd

  - bang - time to measure.

OUTLET:

- bang - output elapsed time.

ARGUMENTS:

- NONE.


> see also [[timer]](../timer) [[cputime]](../cputime)
 
> updated for Pd version 0.33