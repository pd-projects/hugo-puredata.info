---
title: "[float]"
description: "store and recall a number"
bref: "store and recall a number"
categories: ["object", "General"]
draft: false
---

### [float] 

Store a (floating point) number

The float object stores a number, initialized by its creation argument, 
which may be reset using its inlet and output by sending it the "bang" 
message. Sending a number sets a new value and outputs it.

inlet 0

 - bang: outputs the float
 - float: outputs the float
 - symbol: converts to float
 - `send` to a named object

inlet 1

 - float: sets a float without outputting

outlet 0

 - float
 
> see also [[int]](../int) [[value]](../value) [[send]](../send)

> updated for Pd version 0.48
