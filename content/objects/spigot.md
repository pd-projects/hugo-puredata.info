---
title: "[spigot]"
description: "pass or block messages"
bref: "pass or block messages"
draft: false
categories: ["object"]
pdcategory: "General"
---

### [spigot]

Pass or block messages.

Spigot passes messages from its left inlet to its outlet,  as long as a nonzero number is sent to its right inlet. When its right inlet gets zero,  incoming messages are "blocked" i.e.,  ignored.

INLET:

- 1st:

  - anything - any message to pass or not.

- 2nd:

  - float - nonzero to pass messages,  zero to stop them.

OUTLET:

- anything - any input message if spigot is openned.

ARGUMENT:

- float - initialize right inlet.

 
> updated for Pd version 0.38