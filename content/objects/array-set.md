---
title: array set
description: set contents from a list.
categories:
- object
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
inlets:
  1st:
    list: list of values to write to array
  2nd:
   float: onset (index to set from, 0 is the start).
  3rd:
    symbol: set array name.
    pointer: pointer to the array if -s flag is used.
outlets:
  1st:
    list: array's elements.
arguments:
  1) symbol: array name if no flags are given (default none).
  2) float: initial onset (default 0).

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
  -f <symbol, symbol>: struct name and field name of element structure.
draft: false
pdcategory: Arrays & Tables

---

"array set" sets values of an array from an incoming list, starting from a specified onset (0 by default). The size of the array is not changed - values that would be written past the end of the array are dropped.
