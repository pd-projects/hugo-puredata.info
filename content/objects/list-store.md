---
title: list store
description: manipulate lists
categories:
- object
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
  list: initialize the stored list (default empty).
inlets:
  1st:
    list: concatenate incoming list with stored list and output (a bang is a zero element list and outputs stored list).
    prepend <list>: prepend a list to the stored list.
    append <list>: append a list to the stored list.
    get <list>: output an item (if only one float is given) or sublist, where first element sets staring index and the second sets ending index (-1 is end of the list).
    set <list>: set values starting at index from the fisrt element.
    insert <list>: insert values before index from the fisrt element.
    delete <list>: delete a given item for just one float or a number of items specified in the second element starting at index from the first element (-1 means delete all items from given index).
    send <symbol>: send stored list to a named receiver.
  2nd:
    anything: set stored list (a bang is a zero element list and clears it).


outlets:
  1st:
    list: the stored list.
draft: false
pdcategory: General

---
Put together or break apart a list to/from sublists
