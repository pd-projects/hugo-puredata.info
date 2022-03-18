---
title: "[list]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object", "General"]
---

### [list]

Manipulate lists.

Short for "list append"

ARGUMENTS:

- symbol - sets the function of [list], possible values: append, prepend, store, split, trim, length, fromsymbol and tosymbol. The default value is 'append'.

[[list append]](#list-append)\
[[list prepend]](#list-prepend)\
[[list store]](#list-store)\
[[list split]](#list-split)\
[[list trim]](#list-trim)\
[[list length]](#list-length)\
[[list fromsymbol]](#list-fromsymbol)\
[[list tosymbol]](#list-tosymbol)

------------------

### [list append]

Use list append to concatenate a second list (defined via arguments or the right inlet) to the first list via the left inlet.

INLETS

- 1st:

  - anything - set messages to concatenate to a second list and output (a bang is a zero element list).

- 2nd:

  - anything - set messages to append to the first list (a bang is a zero element list and clears it).

OUTLET:

- list - the concatenated list.

ARGUMENTS:

- list - initialize the list to append (default empty).
 
----------------------

### [list prepend]

Use list prepend to prepend a second list (defined via arguments or the right inlet) to the first list via the left inlet.

INLETS

- 1st:

  - anything - set messages to be prepended by a second list and output (a bang is a zero element list).

- 2nd:

  - anything - set messages to prepend to the first list (a bang is a zero element list and clears it).

OUTLET:

- list - the prepended list.

ARGUMENTS:

- list - initialize the list to prepend (default empty).

---------------

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

------------------

### [list split]

Cut a list into smaller ones.

The "list split" object takes lists and outputs the first "n" items (left outlet) and the remaining ones (middle outlet). If the incoming list also has 'n' items, the middle outlet spits a list with zero elements (which becomes a bang). The two outputs appear in the usual right-to-left order. In case there are fewer than "n" items in the list, it is output (in its entirety) from the third outlet instead. The creation argument or the inlet sets the split point.

INLETS

- 1st:

  - anything - messages to be split into smaller lists.

- 2nd:

  - float - sets new 'n' split point.

OUTLET:

- 1st:

  - list - the first 'n' elements of the list.

- 2nd:

  - list - the remaining portion of the list.

- 3rd:

  - list - if incoming list is shorter than n.

ARGUMENTS:

- float - initialize split point.

---------------------

### [list trim]

Remove list selector.

The "list trim" object inputs lists (or makes lists out of incoming non-list messages) and outputs a message whose selector is the first item of the list, and whose arguments, if any, are the remainder of the list. If the list has no items, or if its first item is numeric, the selector is "list" (which might print out as list, float, or bang.)

INLETS

- list - list messages to be trimmed.

- symbol - the symbol selector is also trimmed.

- anything - any other messages are output intact.

OUTLET:

- anything - trimmed list.


ARGUMENTS:

- NONE.

----------------------------------

### [list length]

Number of items in list.

The "list length" object outputs the number of arguments in a list or other message.

INLETS

- anything - messages to have its elements counted.

OUTLET:

- float - list length.

ARGUMENTS:

- NONE.

-----------------------------

The folowing `[list fromsymbol]` and `[list tosymbol]` allow you to do string manipulations (such as scanning a filename for '/' characters). They convert a list of numbers (which might be ASCII or might be unicode if, for example, they represent a filename on a non-ASCII machine) to or from a symbol.

### [list fromsymbol]

Convert from symbols to lists of numeric character codes

INLETS

- symbol - symbol to be converted to a list of character codes.

OUTLET:

- list - list of converted character codes.

ARGUMENTS:

- NONE.

-------------------------

### [list tosymbol]

Convert from list of numeric character codes to symbols.

INLETS

- list - list of character codes to convert to a symbol.

OUTLET:

- symbol - converted symbol from list of character codes.

ARGUMENTS:

- NONE.


