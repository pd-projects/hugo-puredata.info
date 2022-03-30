---
title: text define
description: create, store, and/or edit texts
categories:
- object
pdcategory: Misc
last_update: '0.49'
see_also:
- list
- array
- scalar
- text
- text get
- text set
- text insert
- text delete
- text size
- text tolist
- text fromlist
- text search
- text sequence
arguments:
- type: symbol
  description: set text name.
flags:
- flag: -k
  description: saves/keeps the contents of the text with the patch.
inlets:
  1st:
    bang: output a pointer to the scalar containing the text.
    clear: clear contents of the text.
    click: open text window.
    close: closes the text window.
    read <symbol>: read from a file (with optional -c flag).
    send <symbol>: send pointer to a named receive object
    sort: sort the text contents.
    write <symbol>: write to a file (with optional -c flag).
outlets:
  1st:
    pointer: a pointer to the scalar containing the array.
  2nd:
    anything: outputs "updated" when text changes.
draft: false
---
"text define" maintains a text object and can name it so that other objects can find it (and later should have some alternative, anonymous way to be found).

an optional `-c` flag allows you to read or write to/from a file interpreting carriage returns as separators.
