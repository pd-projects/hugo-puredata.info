---
title: array define
description: create an array.
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.52'
see_also:
- array
- array size
- array sum
- array get
- array set
- array quantile
- array random
- array max
- array min
- text
- scalar
- list
arguments:
- type: 1) symbol
  description: array name (default = internal numbered 'table#').
- type: 2) float
  description: size and also xrange (default = 100).
flags:
- flag: -k
  description: saves/keeps the contents of the array with the patch.
- flag: -yrange <float, float>
  description: set minimum and maximum plot range.
- flag: -pix <float, float>
  description: set x and y graph size.
inlets:
  1st:
    bang: output a pointer to the scalar containing the array.
    other messages: '[array define] send other messages that arrays understand like
      ''const'', ''resize'', etc. For reference, see 2.control.examples ''15.array''
      and ''16.more.arrays''.'
    send <symbol>: send pointer to a named receive object.
outlets:
  1st:
    pointer: a pointer to the scalar containing the array.
draft: false
---
"array define" maintains an array and can name it so that other objects can find it (and later should have some alternative, anonymous way to be found).
