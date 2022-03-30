---
title: text
description: manage a list of messages
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
- text tolist
- text fromlist
- text search
- text sequence
arguments:
- type: symbol
  description: 'sets the function of [text], possible values: define, get, set, insert,
    delete, size, tolist, fromlist, search and sequence. The default value is ''define''.'
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

