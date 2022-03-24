---
title: "[delay]"
description: "send a message after a time delay"
bref: "send a message after a time delay"
draft: false
categories: ["object"]
pd-category: "Time"
---

### [delay]

send a bang message after a time delay

The delay object outputs a bang after a given delay time (via argument or right inlet). A bang starts the delay. A float specifies the time delay and starts it. If the delay is running and scheduled to output, sending a bang or a float cancels the previous setting and reschedules the output.

Delay times are in units of 1 millisecond by default, but you can change this with the second and third argument or with a "tempo" message (as in [timer], [metro] and [text sequence]), which set a tempo value and a time unit symbol. Possible symbols are:

- millisecond (msec for short)
- seconds (sec)
- minutes (min)
- samples (samp)

These symbols can also be preceeded by "per" (as in "permin",  "permsec",  etc.) In this case,  60 permin means 1/60 min (hence,  the same as 'BPM').

'samp' depends on the sample rate the patch is running


INLETS:

- 1st:

  - float - set delay time and start the delay.

  - bang - start the delay.

  - stop - stop the delay.

  - tempo &lt;float,  symbol&gt; - set tempo value (float) and time unit symbol.

- 2nd: 

  - float - set delay time for the next tempo.

OUTLET:

- bang - bang at a delayed time.

ARGUMENTS:

- float - initial delay time (default 0).

- float - tempo value (default 1).

- symbol - time unit (default 'msec').


 
> see also [[metro]](../metro) [[pipe]](../pipe) [[text sequence]](../#) [[timer]](../timer)
 
> updated for Pd version 0.45
