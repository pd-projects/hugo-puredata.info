---
title: text sequence
description: sequencer/message-sender.
categories:
- object
see_also:
- list
- array
- scalar
- text define
- text get
- text set
- text insert
- text delete
- text size
- text tolist
- text fromlist
- text search
- text
last_update: '0.49'
inlets:
  1st:
    auto: automatically sequence interpreting waits as delay times.
    stop: stops the sequence when in auto mode.
    step: output next line.
    line <float>: set line number (counting from 0).
    args <list>: set values for $1, $2, etc in the text.
    bang: output all lines from current to next waiting point.
    list: same as bang but temporarily override 'args' with list's elements (a bang is a 0 element list, btw).
    tempo <f, sym>: set tempo value (float) and time unit symbol.
  2nd:
    symbol: set text name.
    pointer: pointer to the text if -s flag is used.
outlets:
  1st:
    list: messages from the sequence or waits if -g flag is given.
  2nd:
    list: waits if -w flag is given (which creates a mid outlet).
  rightmost:
    bang: when finishing the sequence.
flags:
  -s <symbol, symbol>: struct name and field name of main structure.
  -g: sets to global mode (with symbolic destinations).
  -w <symbol>: sets symbols that define waiting points.
  -w <float>: sets number of leading floats used as waiting points.
  -t <float, symbol>: sets tempo value and time unit.
arguments:
  symbol: "text name if no flags are given (default: none)."

draft: false
pdcategory: Misc

---

"text sequence" outputs lines from a text buffer, either to an outlet or as messages to named destinations. The text is interpreted as a sequence of lists, and possibly some interspersed waiting instructions (called "waits" here). You can ask for one line at a time ("step" message), or to proceed without delay to the next wait ("bang"), or to automatically sequence through a series of waits (with each wait specifying a delay in milliseconds).
