---
title: text define
description: create, store, and/or edit texts
categories:
- object
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
last_update: '0.49'
inlets:
  1st:
    bang: output a pointer to the scalar containing the text.
    clear: clear contents of the text.
    send <symbol>: send pointer to a named receive object
    read <symbol>: read from a file (with optional -c flag).
    write <symbol>: write to a file (with optional -c flag).
    sort: sort the text contents.
    click: open text window.
    close: closes the text window.
outlets:
  1st:
    pointer: a pointer to the scalar containing the array.
  2nd:
    anything: outputs "updated" when text changes.
flags:
  -k: saves/keeps the contents of the text with the patch.
arguments:
  1) symbol: set text name.
draft: false
pdcategory: Misc

---

"text define" maintains a text object and can name it so that other objects can find it (and later should have some alternative, anonymous way to be found).

an optional `-c` flag allows you to read or write to/from a file interpreting carriage returns as separators.
