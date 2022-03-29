---
title: text size
description: get number of lines or elements.
categories:
- object
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
last_update: '0.49'
inlets:
  1st:
    bang: output the number of lines.
    float: set line number and output its length.
  2nd:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.
outlets:
  1st:
    float: number of lines or line length.
flags:
  -s <symbol, symbol>: struct name and field name of main structure.
arguments:
  symbol: "text name if no flags are given (default: none)."

  
draft: false
pdcategory: Misc

---

"text size" reports the number of lines in the text or the length of a specified line.
