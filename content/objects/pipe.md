---
title: "[pipe]"
description: "dynamically growable delay line for numbers"
bref: "dynamically growable delay line for numbers"
draft: false
categories: ["object"]
pdcategory: "Time"
---

### [pipe]

Message "delay line".

The [pipe] object stores a sequence of messages and outputs them after a specified delay time in milliseconds. The output is scheduled when storing the incoming message. Thus changing the delay time doesn't affect the messages that are already scheduled.

You can specify the data type with a first argument (which is a float by default). A symbol argument "s", "f", or "p" specifies a "symbol", "float" (number), or pointer type (untested). The delay time comes then as the last argument.

You can specify compound messages (lists) by adding more than one argument.


INLETS:

- 1st:

  - bang - sends the last received data after the delay time.

  - flush - sends the scheduled messages immediately.

  - clear - forget all scheduled messages.
  
  - float/symbol/pointer - the type depends on the creation argument.

- n: number of inlets depends on creation arguments

  - float/symbol/pointer - the type depends on the creation argument.

- rightmost:

  - float - set the delay time in ms.

OUTLETS:



- n: number of inlets depends on creation arguments

  - float/symbol/pointer - the type depends on the creation argument.

ARGUMENTS:

- 1st: list - (optional) symbols sets number of inlets and type (f default,  s,  p) and floats set float type and initial value.

- 2nd: float - sets delay time in ms (default 0).
 
 
 
 
> see also [[delay]](../delay) [[timer]](../timer) 
 
> updated for Pd version 0.33