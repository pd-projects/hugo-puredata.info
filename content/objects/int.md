---
title: "[int]"
description: "store and recall an integer"
bref: "store and recall an integer"
categories: ["object"]
pd-category: "General"
aliases: [ "i"]
draft: false
---

### [int] 

Truncate floats and store an integer

The int object stores a number initialized by its creation argument,  which may be reset using its inlet and output by sending it the "bang" message. Sending a number sets a new value and outputs it. A non-integer input is truncated to an integer (a la Max) so the object can also be used to truncate values and convert from float to integers.



INLETS: 

- 1st: 

  - bang - output the stored value.
  
  - float -store and output the value,  non-integers are truncated.

  - list - considers the first element if it's a float,  stores and outputs it.

  - send &lt;symbol&gt; - send the stored value to a [receive] or [value] object that has the same name as the symbol (no output).


- 2nd: 

  - float - store the value, non-integers are truncated (no output).

OUTLET:

- float - the stored integer value.

ARGUMENT:

- float - initially stored value (default 0).


 
> see also [[float]](../float) [[value]](../value) [[send]](../send-receive)

> updated for Pd version 0.48

