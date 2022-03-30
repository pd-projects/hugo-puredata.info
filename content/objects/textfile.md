---
title: textfile
description: read and write text files
categories:
- object
pdcategory: Misc
last_update: '0.33'
see_also:
- qlist
- text sequence
inlets:
  1st:
    add <anything>: add a message to textfile.
    add2 <anything>: add a message but don't terminate it.
    bang: output a whole line and go to the next
    clear: empty the textfile.
    print: print contents to Pd window.
    read <symbol, cr>: read a file (with optional 'cr' argument).
    rewind: go to beginning (and stop).
    set <anything>: clear and add a message to textfile.
    write <symbol, cr>: write to a file (with optional 'cr' argument).
outlets:
  1st:
    anything: lines stored in the textfile object.
  2nd:
    bang: when reaching the end of sequence.
draft: false
---
'cr' = terminating lines only with carriage return (omitting semicolons.) You can read files this way too, in which case carriage returns are mapped to semicolons.

The textfile object reads and writes text files to and from memory. You can read a file and output sequential lines as lists, or collect lines and write them out. You can use this object to generate "models" for Gem, for instance.

To record textual messages and save them to a file, first send "clear" to empty the qlist and "add" to add messages (terminated with semicolons.) The message, "add2" adds a list of atoms without finishing with a semicolon in case you want to make variable-length messages.

You can also use this object simply for storing heterogeneous sequences of lists.
