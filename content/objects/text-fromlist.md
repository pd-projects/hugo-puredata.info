---
title: text fromlist
description: convert from list.
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
- text
- text search
- text sequence
last_update: '0.49'
inlets:
  1st:
    list: sets contents of text from given list.
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

"text fromlist" converts a list such as "text tolist" would output and fills the text with it. Whatever the text had previously contained is discarded.
