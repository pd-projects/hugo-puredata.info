---
title: array random
description: array as probabilities.
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
- array max
- array min
inlets:
  1st:
    bang: bang to generate a random value.
    seed <float>: sets random seed.
    float: sets onset.
  2nd:
   float: set number of points (-1 is the end of the array).
  3rd:
    symbol: set array name.
    pointer: pointer to the array if -s flag is used.
outlets:
  1st:
    float: random index value from the array.
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

"array random" makes a pseudo-random number from 0 to 1 and outputs its quantile (which will therefore have probabilities proportional to the table's values.)
