---
title: "[symbol]"
description: "store and recall a symbol"
bref: "store and recall a symbol"
categories: ["object", "General"]
draft: false
---

### [symbol] 

Store a symbol (i.e., string)

The symbol object stores a symbol, Pd's data type for handling fixed 
strings (often filenames or the names of other objects in pd).

note: unlike "float", etc., there's no "s" message to forward to 
another object -- that would conflict with the function of converting 
arbitrary messages to symbols.

inlet 0

 - bang: outputs the value
 - `symbol` set and output the value
 - any other message is 'converted'

inlet 1

 - symbol: set the value

outlet 0

 - symbol
 
> updated for Pd version 0.45
