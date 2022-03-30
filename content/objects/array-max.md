---
title: array max
description: output maximum value of an array.
categories:
- object
last_update: '0.52'
see_also:
- array
- array define
- array size
- array sum
- array get
- array set
- array quantile
- array random
- array min
inlets:
  1st:
    bang: to find max
    float: onset (index to output from, 0 is the start).

  2nd:
   float: number or points to output from onset (-1 is the end of array).
  3rd:
    symbol: set array name.
    pointer: pointer to the array if -s flag is used.
outlets:
  1st:
    float: maximum value
  2nd:
    float: index of found value
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

"array max" find the maximum value in the array. The first outlet is the value and the second is the index (the x location where the value was found). The search may be restricted to a sub-domain of the array by specifying the "onset" and "number of points".
