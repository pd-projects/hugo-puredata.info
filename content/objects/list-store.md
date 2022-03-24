---
title: "[list store]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object"]
pdcategory: "General"
---



### [list store]

Put together or break apart a list to/from sublists

INLETS

- 1st:

  - list - concatenate incoming list with stored list and output (a bang is a zero element list and outputs stored list).
  
  - prepend &lt;list&gt; - prepend a list to the stored list.
  
  - append &lt;list&gt; - append a list to the stored list.
  
  - get &lt;list&gt; - output an item (if only one float is given) or sublist, where first element sets staring index and the second sets ending index (-1 is end of the list).
  
  - set &lt;list&gt; - set values starting at index from the fisrt element.
  
  - insert &lt;list&gt; - insert values before index from the fisrt element.
  
  - delete &lt;list&gt; - delete a given item for just one float or a number of items specified in the second element starting at index from the first element (-1 means delete all items from given index).
  
  - send &lt;symbol&gt; - send stored list to a named receiver.

- 2nd:

  - anything - set stored list (a bang is a zero element list and clears it).

OUTLET:

- list - the stored list.

ARGUMENTS:

- list - initialize the stored list (default empty).

> see also [[list]](../list)\
> [[list append]](../list-append)\
> [[list prepend]](../list-prepend)\
> [[list split]](../list-split)\
> [[list trim]](../list-trim)\
> [[list length]](../list-length)\
> [[list fromsymbol]](../list-fromsymbol)\
> [[list tosymbol]](../list-tosymbol)