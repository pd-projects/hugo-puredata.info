---
title: "[float]"
description: "store and recall a number"
bref: "store and recall a number"
categories: ["object", "General"]
aliases: [ "f" ]
draft: false
---

### [float] 

Store a (floating point) number

The float object stores a number,  initialized by its creation argument,  which may be reset using its inlet and output by sending it the "bang" message. Sending a number sets a new value and outputs it.


INLETS:

- 1st:

  - bang - output the stored value.
  
  - float - store and output the value.
  
  - list - considers the first element if it's a float,  stores and outputs it.
  
  - symbol - symbols that look like a float are converted,  stored and output.
  
  - send &lt;symbol&gt; - send the stored value to a [receive] or [value] object that has the same name as the symbol (no output).


- 2nd:

  - float - store the value (no output).

OUTLET:

- float - the stored value.

ARGUMENT:

- float - initially stored value (default 0).


 
> see also [[int]](../int) [[value]](../value) [[send]](../send-receive) [[symbol]](../symbol) 

> updated for Pd version 0.48
