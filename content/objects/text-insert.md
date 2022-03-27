---
title: text insert
description: insert a line.
categories:
- object
see_also:
- list
- array
- scalar
- text define
- text get
- text set
- text
- text delete
- text size
- text tolist
- text fromlist
- text search
- text sequence
last_update: '0.49'
inlets:
  1st:
    list: a line to insert.
  2nd:
    float: line number to insert.
  3rd:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
arguments:
  symbol: "text name if no flags are given (default: none)."
  float: "set line number (default: 0)."
  
draft: false
pdcategory: Misc

---


