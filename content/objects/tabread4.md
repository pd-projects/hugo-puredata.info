---
title: tabread4
description: read a number from a table
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.43'
see_also:
- tabplay~
- tabread
- tabreceive~
- tabsend~
- tabwrite
- tabwrite~
arguments:
- type: symbol
  description: sets table name with the sample.
inlets:
  1st:
    float: sets table index and output its value with interpoation.
    set <symbol>: set the table name.
outlets:
  1st:
    float: value of index input.
draft: false
---
The tabread4 object reads values from an array ("table") according to an index,  applying four-point polynomial interpolation. Indices should range from 1 to (size-2) so that the 4-point interpolation is meaningful. Indices outside of the range are replaced by the nearest index in range.

Check also the "array" examples from the Pd tutorial by clicking and opening `doc/2.control.examples/16.more.arrays`.
