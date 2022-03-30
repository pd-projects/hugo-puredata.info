---
title: text search
description: search for a line.
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
- text size
- text tolist
- text fromlist
- text
- text sequence
arguments:
- type: 1) symbol
  description: 'text name if no flags are given (default: none).'
- type: 2) list
  description: search field number optionally preceded by '>'. '>=', '<', '<=', or
    'near'.
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
inlets:
  1st:
    list: search key.
  2nd:
    pointer: pointer to the text if -s flag is used.
    symbol: set text name.
outlets:
  1st:
    float: found line number or -1 if not found.
draft: false
---
"text search" outputs the line number of the line that best matches a search key. By default it seeks a line whose leading fields match the incoming list.
