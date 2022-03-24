---
title: symbol
description: store and recall a symbol
bref: store and recall a symbol
categories:
- object
last_update: '0.45'
see_also:
- print
- int
- float
arguments:
  symbol: 'initially stored symbol (default: empty symbol).'
inlets:
  1st:
    anything: converts to symbol,  stores it and outputs it.
    bang: output the stored symbol.
    symbol: stores the symbol received and outputs it.
  2nd:
    symbol: stores the symbol (no output).
outlets:
  1st:
    symbol: the stored symbol.
pdcategory: General
draft: false

---
Store a symbol (i.e., string)

The symbol object stores a symbol,  Pd's data type for handling fixed strings (often filenames,  array names,  send/receive names or the names of other objects in pd).

NOTE: unlike "float",  etc.,  there's no "send" message to forward to another object -- that would conflict with the function of converting arbitrary messages to symbols.
