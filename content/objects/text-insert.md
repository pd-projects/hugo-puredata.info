---
title: text insert
description: insert a line.
categories:
- object
pdcategory: Misc
last_update: '0.49'
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
arguments:
- type: symbol
  description: 'text name if no flags are given (default: none).'
- type: float
  description: 'set line number (default: 0).'
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
inlets:
  1st:
    list: a line to insert.
  2nd:
    float: line number to insert.
  3rd:
    pointer: pointer to the text if -s flag is used.
    symbol: set text name.
draft: false
---

