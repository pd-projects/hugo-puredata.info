---
title: list
description: manipulate lists
bref: manipulate lists
categories:
- object
see_also:
- list append
- list prepend
- list store
- list split
- list trim
- list length
- list fromsymbol
- list tosymbol
arguments:
  symbol: 'sets the function of [list], possible values: append, prepend, store, split,
    trim, length, fromsymbol and tosymbol. The default value is ''append''.'
inlets:
  1st:
    anything: set messages to concatenate to a second list and output (a bang is a zero element list).
  2nd:
    anything: set messages to append to the first list (a bang is a zero element list and clears it).
outlets:
  1st:
    list: the concatenated list.
draft: false
pdcategory: General

---
Short for "list append"


