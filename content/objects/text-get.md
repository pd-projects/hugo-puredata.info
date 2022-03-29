---
title: text get
description: read and output a line.
categories:
- object
see_also:
- list
- array
- scalar
- text define
- text
- text set
- text insert
- text delete
- text size
- text tolist
- text fromlist
- text search
- text sequence
last_update: '0.49'
inlets:
  1st:
    float: specify line number and output (0 for first line).
  2nd:
    float: starting field number (-1 for the whole line).
  3rd:
    float: specify number of fields.
  4th:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.
outlets:
  1st:
    list: a line from text or fields from a line.
  2nd:
    float: "line type: 0 if terminated by a semicolon, 1 if by a comma, or 2 if the line number was out of range."
flags:
  -s <symbol, symbol>: struct name and field name of main structure.
arguments:
  symbol: "text name if no flags are given (default: none)."
  float: "starting field number (default: 0)."
  float: "initial number of fields (default: 1)."
  
draft: false
pdcategory: Misc

---

"text get" reads the nth line from the named text and outputs it, or optionally reads one or more specific fields (atoms) from the line.
