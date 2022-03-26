---
title: tabread
description: read a number from a table
categories:
- object
last_update: '0.43'
see_also:
- tabplay~
- tabread4
- tabreceive~
- tabsend~
- tabwrite
- tabwrite~
arguments:
  symbol: sets table name with the sample.
inlets:
  1st:
    float: sets table index and output its value.
    set <symbol>: set the table name.
outlets:
  1st:
    float: value of index input.
draft: false
pdcategory: Arrays & Tables

---
The tabread object reads values from an array ("table") according to an index. The index is rounded down to the next lower integer. Values in the table correspond to indices starting at 0 Indices outside of the range are replaced by the nearest index in range.

Check also the "array" examples from the Pd tutorial by clicking and opening `doc/2.control.examples/16.more.arrays`
