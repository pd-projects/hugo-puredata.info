---
title: array define
description: create an array.
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
- array max
- array min
inlets:
  1st:
    bang: output a pointer to the scalar containing the array.
    send <symbol>: send pointer to a named receive object.
    other messages: "[array define] send other messages that arrays understand like 'const', 'resize', etc. For reference, see 2.control.examples '15.array' and '16.more.arrays'." 
outlets:
  1st: 
    pointer: a pointer to the scalar containing the array.
arguments:
  1) symbol: array name (default = internal numbered 'table#'). 
  2) float: size and also xrange (default = 100).
flags:
  -k: saves/keeps the contents of the array with the patch. 
  -yrange <float, float>: set minimum and maximum plot range.
  -pix <float, float>: set x and y graph size.
draft: false
pdcategory: Arrays & Tables

---

