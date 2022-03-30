---
title: text delete
description: delete a line or clear.
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
- text insert
- text
- text size
- text tolist
- text fromlist
- text search
- text sequence
arguments:
- type: symbol
  description: 'text name if no flags are given (default: none).'
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
inlets:
  1st:
    float: line number to delete (negative deletes all lines).
  2nd:
    pointer: pointer to the text if -s flag is used.
    symbol: set text name.
draft: false
---
"text delete" deletes the nth line.
