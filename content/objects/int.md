---
title: "[int]"
description: "store and recall an integer"
bref: "store and recall an integer"
categories: ["object", "General"]
draft: false
---

### [int] 

Store an integer

The int object stores a number, initialized by its creation argument, 
which may be reset using its inlet and output by sending it the "bang" 
message. Sending a number sets a new value and outputs it. The output 
is truncated to an integer a la Max.



inlet 0

 - bang: outputs the value
 - float: set and output the value
 - `send` to a named object

inlet 1

 - float: set the value

outlet 0

 - float
 
> see also [[float]](../float) [[value]](../value) [[send]](../send)

> updated for Pd version 0.48

