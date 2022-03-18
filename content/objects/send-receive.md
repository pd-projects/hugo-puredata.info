---
title: "[send] & [receive]"
description: "Send and receive messages without patch cords."
bref: "Send and receive messages without patch cords."
categories: ["object", "General"]

draft: false
---

### [send] & [receive]

Send and receive messages without patch cords.

--------------

### [send]

Send messages without patch cords.

[Send] sends messages to "receive" objects. Sends and receives are named to tell them whom to connect to. They work across windows too. 


INLETS:

- 1st: 

  - any message - sends to the corresponding receive object,  or any named object which name corresponds to the stored symbol. e.g: array,  value,  iemguis,  directly to a named patch,  etc...

- 2nd: (if created without arguments)

  - symbol - sets the send name.

OUTLETS:

- NONE

ARGUMENT:

- symbol - send symbol (if given,  2nd inlet is suppressed,  default: empty symbol)

-----------------

### [receive]

Receive messages without patch cords

The [receive] object gets messages directly from [send] or other objects like [list store], [float], [int] and [value] via a `send` method.

INLETS:

- NONE

OUTLET:

- any message - outputs the messages destined to its receive name.


ARGUMENT:

- symbol - receive name symbol (default: empty symbol)

------------------ 

> see also [[send~]](../send~) [[receive~]](../receive~) [[samplerate~]](../samplerate~)
 
> updated for Pd version 0.48
 


