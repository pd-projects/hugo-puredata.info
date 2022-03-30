---
title: text size
description: get number of lines or elements.
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
- text delete
- text
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
    bang: output the number of lines.
    float: set line number and output its length.
  2nd:
    pointer: pointer to the text if -s flag is used.
    symbol: set text name.
outlets:
  1st:
    float: number of lines or line length.
draft: false
---
"text size" reports the number of lines in the text or the length of a specified line.
