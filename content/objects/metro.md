---
title: "[metro]"
description: "send a message periodically"
bref: "send a message periodically"
draft: false
categories: ["object"]
pdcategory: "Time"
---

### [metro]

Send a bang message periodically (a la metronome).

The metro object sends a series of bangs at regular time intervals. The left inlet takes a nonzero number or "bang" to start and 0 or 'stop' to stop it. The time is set via the right inlet or first argument. The default time unit is 1 millisecond but you can change this via the 2nd and 3rd argument or the "tempo" message (as in [timer],  [delay] and [text sequence]),  which set a different tempo number and a time unit symbol. Possible symbols are:

- millisecond (msec for short) 
- seconds (sec)
- minutes (min
- samples (samp)

These symbols can also be preceded by "per" (as in "permin",  "permsec",  etc.) In this case,  60 permin means 1/60 min (hence,  the same as 'BPM'). 'samps' depends on the sample rate the patch is running.

INLETS:

- 1st:

  - float - non zero starts and zero stops the metronome.

  - bang - start the metronome.

  - stop - stop the metronome.

  - tempo &lt;float,  symbol&gt; - set tempo value (float) and time unit symbol.

- 2nd:

  - float - set metronome time for the next tempo.

OUTLET:

- bang - bang at a periodic time.

ARGUMENT:

- float - initial metronome time (default 0).

- float - tempo value (default 1).

- symbol - time unit (default 'msec').



> see also [[delay]](../delay) [[text sequence]](../#) [[timer]](../timer)


> Updated for Pd version 0.48
 
