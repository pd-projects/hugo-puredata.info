---
title: print
description: print messages to terminal window
bref: print messages to terminal window
categories:
- object
see_also:
- print~
arguments:
  list: message to distinct one [print] from another.
inlets:
  1st:
    anything: any message to print into the terminal window.
draft: false
pdcategory: General

---
Print prints out the messages it receives on the "terminal window" that Pd is run from. If no argument is given,  the message has a "print:" prefix. Any message as an argument is used as the prefix instead (so you can differentiate between different printouts).

You can also do command/control + click on the terminal window and the corresponding [print] object will be selected in your patch.

With the special "-n" flag the default "print:" prefix is suppressed.
