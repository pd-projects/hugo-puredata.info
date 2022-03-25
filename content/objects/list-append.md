---
title: list append
description: manipulate lists
categories:
- object
see_also:
- list
- list prepend
- list store
- list split
- list trim
- list length
- list fromsymbol
- list tosymbol
arguments:
  list: initialize the list to append (default empty).
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
aliases:
- list

---
Use list append to concatenate a second list (defined via arguments or the right inlet) to the first list via the left inlet.
