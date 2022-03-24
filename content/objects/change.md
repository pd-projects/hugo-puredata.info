---
title: "[change]"
description: "remove repeated numbers from a stream"
bref: "remove repeated numbers from a stream"
draft: false
categories: ["object"]
pd-category: "General"
---

### [change]

Remove repeated numbers from a stream

The change object outputs its input only when it changes. You can "set" the current value,  or bang to force output.

INLET:

- float - input value (repeated numbers are filtered).

- bang - output current value.

- set &lt;float&gt; - set the value.

OUTLET:

- float - unrepeated value.

ARGUMENTS:

- float - initial value (default 0).


 
> updated for Pd version 0.27