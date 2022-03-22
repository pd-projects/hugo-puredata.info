---
title: "[receive]"
description: "Receive messages without patch cords."
bref: "Receive messages without patch cords."
categories: ["object", "General"]

draft: false
---

### [receive]

Receive messages without patch cords

The [receive] object gets messages directly from [send] or other objects like [list store], [float], [int] and [value] via a `send` method.

INLETS:

- NONE

OUTLET:

- any message - outputs the messages destined to its receive name.


ARGUMENT:

- symbol - receive name symbol (default: empty symbol)


> see also [[send~]](../send~) [[receive~]](../receive~) [[samplerate~]](../samplerate~)
 
> updated for Pd version 0.48
 


