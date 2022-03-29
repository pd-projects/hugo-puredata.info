---
title: text tolist
description: convert text to a list.
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
- text 
- text fromlist
- text search
- text sequence
last_update: '0.49'
inlets:
  1st:
    bang: output contents as a list.
  2nd:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.
outlets:
  1st:
    list: contents of text as a list.
flags:
  -s <symbol, symbol>: struct name and field name of main structure.
arguments:
  symbol: "text name if no flags are given (default: none)."

  
draft: false
pdcategory: Misc

---

"text tolist" outputs the entire contents as a list. Semicolons, commas, and dollar signs are output as symbols (and so, if symbols like ", " are encountered, they're escaped with backslashes).
