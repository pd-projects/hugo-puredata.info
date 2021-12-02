---
title: "[send]"

draft: false
---

### [send]

Send messages without patch cords.

[send] sends messages to [[receive]](receive) objects. Sends and receives 
are named to tell them whom to connect to. They work across windows 
too. Also, you can use message boxes as shown:

````
;
help-send1 34;
help-send2 67
````

If invoked without an argument, "send" creates an inlet to let you 
set the target via "symbol" messages.

The [[value]](../value) object receives float values for variables with the 
same name.

inlet 0

 - anything

inlet 1

- `symbol`

> see also [[float]](../float) [[receive]](../receive) [[value]](../value)

> updated for Pd version 0.48
 


