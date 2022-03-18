---
title: "[trace]"
description: "message tracing for debugging"
bref: "message tracing for debugging"
draft: false
categories: ["object", "General"]
---

### [trace]

Message tracing for debugging.

When 'set-tracing' is on and the object is armed,  trace prints in the Pd window the message it receives and also outputs the messages all the other objects further down in the chain send. You can control-click on the printout to select in the patch the object that caused the message. Once this is done,  trace also prints a backtrace of messages leading up to the one that has set it off.

INLETS:

- 1st:

  - anything - any message to be traced from this point on.

- 2nd:

  - float - arms the object for the given number of messages.

OUTLET:

- anything - bypasses the input message further down the chain.

ARGUMENTS:

- NONE
 
> updated for Pd version 0.52