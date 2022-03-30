---
title: array set
description: set contents from a list.
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.52'
see_also:
- array
- array define
- array size
- array sum
- array get
- array quantile
- array random
- array max
- array min
arguments:
- type: symbol
  description: array name if no flags are given (default none).
- type: float
  description: initial onset (default 0).
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
- flag: -f <symbol, symbol>
  description: struct name and field name of element structure.
inlets:
  1st:
    list: list of values to write to array
  2nd:
    float: onset (index to set from, 0 is the start).
  3rd:
    pointer: pointer to the array if -s flag is used.
    symbol: set array name.
outlets:
  1st:
    list: array's elements.
draft: false
---
"array set" sets values of an array from an incoming list, starting from a specified onset (0 by default). The size of the array is not changed - values that would be written past the end of the array are dropped.
