---
title: text delete
description: delete a line or clear.
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
- text
- text size
- text tolist
- text fromlist
- text search
- text sequence
last_update: '0.49'
inlets:
  1st:
    float: line number to delete (negative deletes all lines).
  2nd:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
arguments:
  symbol: "text name if no flags are given (default: none)."

  
draft: false
pdcategory: Misc

---

"text delete" deletes the nth line.


