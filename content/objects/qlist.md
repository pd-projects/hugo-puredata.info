---
title: qlist
description: text-based sequencer
categories:
- object
see_also:
- textfile
- text sequence
last_update: '0.35'
inlets:
  1st:
    bang: start sequence automatically.
    tempo <float>: set relative tempo.
    rewind: go to beginning (and stop).
    next <float>: single-step forward, optional float suppresses message sending.
    print: print contents to Pd window.
    clear: empty the qlist.
    add <anything>: add a message to a qlist.
    add2 <anything>: add a message to a qlist but don't terminate it.
    read <symbol>: read a file into qlist.
    write <symbol>: write contents to a file.    
outlets:
  1st:
    list: list of leading numbers for the next message.
  2nd:
    bang: when reaching the end of sequence.
draft: false
pdcategory: Misc

---

The qlist object reads text files containing time-tagged Pd messages. You can have them sequenced automatically (by sending a "bang" message, possibly changing speed via "tempo" messages) or manually via the "rewind" and "next" messages.

To run the qlist automatically, send it a "read" message (the filename is relative to the directory the patch is in) and later a "bang." Messages in the file are separated by semicolons. Optional leading numbers are delay times in milliseconds. If the tempo is different from 1 the messages are sent faster or slower accordingly. Messages should start with a symbol giving the destination object. In the file "qlist.q" used here, the messages go to objects "this" and "that" which are receives below.

To run it manually, send "rewind" followed by "next". All messages not preceded by numbers are sent. As soon as a message starting with one or more numbers is encountered, the numbers are output as a list. There are many ways you could design a sequencer around this.

You can also record textual messages and save them to a file. Send "clear" to empty the qlist and "add" to add messages (terminated with semicolons.) The message, "add2" adds a list of atoms without finishing with a semicolon in case you want to make variable-length messages.
