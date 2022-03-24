---
title: "[timer]"
description: "measure time intervals"
bref: "measure time intervals"
draft: false
categories: ["object"]
pd-category: "Time"
---

### [timer]

Measure logical time.

The timer object measures elapsed logical time. Logical time moves forward as if all computation were instantaneous and as if all "delay" and "metro" objects were exact. By default,  the time unit is 1 millisecond,  but you can change this with the 'tempo' message (as in [delay],  [metro] and [text sequence]),  which takes a different tempo number and a time unit symbol. Possible symbols are:

- millisecond (msec for short) 
- seconds (sec) 
- minutes (min) 
- samples (samp) - depends on the sample rate the patch is running

These symbols can also be preceded by "per" (as in "permin",  "permsec",  etc.) In this case,  60 permin means 1/60 min (hence,  the same as 'BPM').

Note you need to reset the elapsed time to zero when you change the tempo message when the object is running,  otherwise you get funny results because the change takes effect immediately and gets applied to the remaining part of the elapsed time.

INLET:

- 1st

  - bang - reset (set elapsed time to zero).

  - tempo &lt;float,  symbol&gt; - set tempo value (float) and time unit symbol.

- 2nd

  - bang - time to measure.
  
OUTLET:

- bang - output elapsed time.

ARGUMENTS:

- float - tempo value (default 1).

- symbol - time unit (default 'msec').
 
> see also [[cputime]](../cputime) [[realtime]](../realtime) [[delay]](../delay) [[metro]](../metro) [[text sequence]](../#)
 
> updated for Pd version 0.47
