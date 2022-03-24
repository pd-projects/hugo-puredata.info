---
title: "[tabread4]"
description: "read a number from a table"
bref: "read a number from a table"
draft: false
categories: ["object"]
pd-category: "Arrays & Tables"
---

### [tabread4]

The tabread4 object reads values from an array ("table") according to an index,  applying four-point polynomial interpolation. Indices should range from 1 to (size-2) so that the 4-point interpolation is meaningful. Indices outside of the range are replaced by the nearest index in range.

Check also the "array" examples from the Pd tutorial by clicking and opening `doc/2.control.examples/16.more.arrays`.



INLET:

- float - sets table index and output its value with interpoation.

- set &lt;symbol&gt; - set the table name. 

OUTLET:

- float - value of index input.

ARGUMENT:

- symbol - sets table name with the sample.
 
> see also [[tabplay~]](../tabplay~) [[tabread]](../tabread) [[tabreceive~]](../tabreceive~) 

> [[tabsend~]](../tabsend~) [[tabwrite]](../tabwrite) [[tabwrite~]](../tabwrite~)
 
 
> updated for Pd version 0.43
