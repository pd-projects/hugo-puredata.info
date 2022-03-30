---
title: array get
description: get contents as a list.
categories:
- object
last_update: '0.52'
see_also:
- array
- array define
- array size
- array sum
- array set
- array quantile
- array random
- array max
- array min
inlets:
  1st:
    bang: output the elements of the array.
    float: onset (index to output from, 0 is the start).
  2nd:
   float: number or points to output from onset (-1 is the end of array).
  3rd:
    symbol: set array name.
    pointer: pointer to the array if -s flag is used.
outlets:
  1st:
    list: array's elements.
arguments:
  1) symbol: array name if no flags are given (default none).
  2) float: initial onset (default 0).
  3) float: initial number of points (default -1, end of array).

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
  -f <symbol, symbol>: struct name and field name of element structure.
draft: false
pdcategory: Arrays & Tables

---

"array get" outputs all or a selected range of elements of the array as a list.
