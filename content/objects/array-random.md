---
title: array random
description: array as probabilities.
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
- array set
- array quantile
- array max
- array min
arguments:
- type: 1) symbol
  description: array name if no flags are given (default none).
- type: 2) float
  description: initial onset (default 0).
- type: 3) float
  description: initial number of points (default -1, end of array).
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
- flag: -f <symbol, symbol>
  description: struct name and field name of element structure.
inlets:
  1st:
    bang: bang to generate a random value.
    float: sets onset.
    seed <float>: sets random seed.
  2nd:
    float: set number of points (-1 is the end of the array).
  3rd:
    pointer: pointer to the array if -s flag is used.
    symbol: set array name.
outlets:
  1st:
    float: random index value from the array.
draft: false
---
"array random" makes a pseudo-random number from 0 to 1 and outputs its quantile (which will therefore have probabilities proportional to the table's values.)
