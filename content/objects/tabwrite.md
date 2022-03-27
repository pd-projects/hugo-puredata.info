---
title: tabwrite
description: write a number to a table
categories:
- object
last_update: '0.33'
see_also:
- array
- tabread
- tabread4
- tabwrite~
arguments:
  symbol: sets table name with the sample.
inlets:
  1st:
    float: sets index to write to.
    set <symbol>: set the table name.
  2nd:
    float: sets index to write to.
draft: false
pdcategory: Arrays & Tables

---
Tabwrite writes floats into an array,  input values are set in the left inlet,  while the index is set on the right inlet.
