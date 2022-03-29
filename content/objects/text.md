---
title: text
description: manage a list of messages
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
  symbol: "sets the function of [text], possible values: define, get, set, insert, delete, size, tolist, fromlist, search and sequence. The default value is 'define'."
draft: false
pdcategory: Misc

---
