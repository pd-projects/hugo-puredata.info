---
title: text search
description: search for a line.
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
- text size
- text tolist
- text fromlist
- text
- text sequence
last_update: '0.49'
inlets:
  1st:
    list: search key.
  2nd:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.
outlets:
  1st:
    float: found line number or -1 if not found.

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
arguments:
  1) symbol: "text name if no flags are given (default: none)."
  2) list: "search field number optionally preceded by '>'. '>=', '<', '<=', or 'near'."

  
draft: false
pdcategory: Misc

---

"text search" outputs the line number of the line that best matches a search key. By default it seeks a line whose leading fields match the incoming list.


