---
title: "[print]"
description: "print messages to terminal window"
bref: "print messages to terminal window"
draft: false
categories: ["object", "General"]
---

### [print]

Print messages to terminal window.

Print prints out the messages it receives on the "terminal window" that Pd is run from. If no argument is given,  the message has a "print:" prefix. Any message as an argument is used as the prefix instead (so you can differentiate between different printouts).

You can also do command/control + click on the terminal window and the corresponding [print] object will be selected in your patch.

With the special "-n" flag the default "print:" prefix is suppressed.

INLET:

- anything - any message to print into the terminal window.

OUTLET:

- NONE

ARGUMENTS:

- list - message to distinct one [print] from another.


 
> see also [[print~]](../print~)

> Updated for Pd version 0.52