---
title: "[symbol]"
description: "store and recall a symbol"
bref: "store and recall a symbol"
categories: ["object"]
pd-category: "General"
draft: false
---

### [symbol] 

Store a symbol (i.e., string)

The symbol object stores a symbol,  Pd's data type for handling fixed strings (often filenames,  array names,  send/receive names or the names of other objects in pd).

NOTE: unlike "float",  etc.,  there's no "send" message to forward to another object -- that would conflict with the function of converting arbitrary messages to symbols.

INLETS:

- 1st:

  - bang - output the stored symbol.

  - symbol - stores the symbol received and outputs it.

  - anything - converts to symbol,  stores it and outputs it.

- 2nd:

  - symbol - stores the symbol (no output).

OUTLET:

- symbol - the stored symbol.

ARGUMENT:

- symbol - initially stored symbol (default: empty symbol).


> see also [[print]](../print) [[int]](../int) [[float]](../float) 
 
> updated for Pd version 0.45
