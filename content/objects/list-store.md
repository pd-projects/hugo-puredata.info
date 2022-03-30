---
title: list store
description: manipulate lists
categories:
- object
pdcategory: General
see_also:
- list
- list append
- list prepend
- list split
- list trim
- list length
- list fromsymbol
- list tosymbol
arguments:
- type: list
  description: initialize the stored list (default empty).
inlets:
  1st:
    append <list>: append a list to the stored list.
    delete <list>: delete a given item for just one float or a number of items specified
      in the second element starting at index from the first element (-1 means delete
      all items from given index).
    get <list>: output an item (if only one float is given) or sublist, where first
      element sets staring index and the second sets ending index (-1 is end of the
      list).
    insert <list>: insert values before index from the fisrt element.
    list: concatenate incoming list with stored list and output (a bang is a zero
      element list and outputs stored list).
    prepend <list>: prepend a list to the stored list.
    send <symbol>: send stored list to a named receiver.
    set <list>: set values starting at index from the fisrt element.
  2nd:
    anything: set stored list (a bang is a zero element list and clears it).
outlets:
  1st:
    list: the stored list.
draft: false
---
Put together or break apart a list to/from sublists
