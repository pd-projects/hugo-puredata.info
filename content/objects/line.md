---
title: "[line]"
description: "send a series of linearly stepped numbers"
bref: "send a series of linearly stepped numbers"
draft: false
categories: ["object", "Time"]
---

### [line]

Ramp generator.

The line object takes values for target/time/grain and ramps to the specified target over the time given in milliseconds,  updating its output at the "grain rate" (also in milliseconds). A list up to 3 floats distributes the values to the inlets,  as usual in Pd. Note that the middle inlet (that sets the time) does not set values for the next ramp (unlike every other inlet in Pd) - thus,  sending a float to the left inlet without priorly setting a value in the middle inlet causes a jump in the output regardless of whatever time value was specified in some previous message. On the other hand,  setting a grain value persists. A grain value of 0 ir less becomes 20 (the default value). If the line object receives a message specifying some new target before reaching the previous one,  it takes off from its current value.

INLETS:

- 1st:

  - float - set target value and start ramp.

  - stop - stop the ramp.

  - set &lt;float&gt; - set initial ramp value.

- 2nd:

  - float - set next ramp time (cleared when ramp starts).

- 3rd:

  - float - sets time grain in ms.

OUTLET:

- float - ramp values.

ARGUMENTS:

- float - initial ramp value (default 0).

- float - time grain in ms (default 20 ms).
 
COMPATIBILITY NOTE: in Pd versions before 0.48,  a stop message followed by a new ramp message would incorrectly ramp from the previous start. It now ramps from wherever in the previous segment the object was stopped at. To get the old behavior,  set "compatibility" to 0.47 or below in Pd's command line or by a message.
 
> see also [[line~]](../line~) [[vline~]](../vline~)
 
> updated for Pd version 0.48