---
title: text sequence
description: sequencer/message-sender.
categories:
- object
pdcategory: Misc
last_update: '0.49'
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
arguments:
- type: symbol
  description: 'text name if no flags are given (default: none).'
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
- flag: -g
  description: sets to global mode (with symbolic destinations).
- flag: -w <symbol>
  description: sets symbols that define waiting points.
- flag: -w <float>
  description: sets number of leading floats used as waiting points.
- flag: -t <float, symbol>
  description: sets tempo value and time unit.
inlets:
  1st:
    args <list>: set values for $1, $2, etc in the text.
    auto: automatically sequence interpreting waits as delay times.
    bang: output all lines from current to next waiting point.
    line <float>: set line number (counting from 0).
    list: same as bang but temporarily override 'args' with list's elements (a bang
      is a 0 element list, btw).
    step: output next line.
    stop: stops the sequence when in auto mode.
    tempo <f, sym>: set tempo value (float) and time unit symbol.
  2nd:
    pointer: pointer to the text if -s flag is used.
    symbol: set text name.
outlets:
  1st:
    list: messages from the sequence or waits if -g flag is given.
  2nd:
    list: waits if -w flag is given (which creates a mid outlet).
  rightmost:
    bang: when finishing the sequence.
draft: false
---
"text sequence" outputs lines from a text buffer, either to an outlet or as messages to named destinations. The text is interpreted as a sequence of lists, and possibly some interspersed waiting instructions (called "waits" here). You can ask for one line at a time ("step" message), or to proceed without delay to the next wait ("bang"), or to automatically sequence through a series of waits (with each wait specifying a delay in milliseconds).
