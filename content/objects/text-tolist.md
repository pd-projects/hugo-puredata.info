---
title: text tolist
description: convert text to a list.
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
- text
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
    bang: output contents as a list.
  2nd:
    pointer: pointer to the text if -s flag is used.
    symbol: set text name.
outlets:
  1st:
    list: contents of text as a list.
draft: false
---
"text tolist" outputs the entire contents as a list. Semicolons, commas, and dollar signs are output as symbols (and so, if symbols like ", " are encountered, they're escaped with backslashes).
