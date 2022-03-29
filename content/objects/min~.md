---
title: min~
description: binary operators on audio signals
categories:
- object
last_update: "0.27"
see_also:
- +
- cos~
- wrap~
- abs~
- log~
- sqrt~
- pow~
- expr~
inlets:
  1st:
    signal: value to the left side of operation and output.
  2nd:
    float/signal: value to the right side of operation.
outlets:
  1st:
    signal: the result of the operation.
  
arguments:
  float: "initialize value of right inlet and makes it only take floats instead of signals (default 0)."
draft: false
pdcategory: Audio Math

---

This object combine two signals as above, or, if you give a numeric argument, the right inlet only takes floats (no signals) and the argument initializes the right inlet value.


