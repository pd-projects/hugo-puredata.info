---
title: "[tabread]"
description: "read a number from a table"
bref: "read a number from a table"
draft: false
categories: ["object", "Arrays & Tables"]
---

### [tabread]

The tabread object reads values from an array ("table") according to an index. The index is rounded down to the next lower integer. Values in the table correspond to indices starting at 0 Indices outside of the range are replaced by the nearest index in range.

Check also the "array" examples from the Pd tutorial by clicking and opening `doc/2.control.examples/16.more.arrays` 



INLET:

- float - sets table index and output its value.

- set &lt;symbol&gt; - set the table name.

OUTLET:

- float - value of index input.

ARGUMENT:

- symbol - sets table name with the sample.


 
> see also [[tabplay~]](../tabplay~) [[tabread4]](../tabread4) [[tabreceive~]](../tabreceive~) 

> [[tabsend~]](../tabsend~) [[tabwrite]](../tabwrite) [[tabwrite~]](../tabwrite~) 
 
> updated for Pd version 0.43