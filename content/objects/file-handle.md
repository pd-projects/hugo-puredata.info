---
title: file handle
description: operate on file handles.
categories:
- object
aliases:
- file
last_update: '0.52'
see_also:
- text
- array
- list
- file
- file define
- file mkdir
- file which
- file glob
- file stat
- file isfile
- file isdirectory
- file size
- file copy
- file move
- file delete
- file split
- file join
- file splitext
- file splitname
inlets:
  1st: 
    open <symbol>: open a file.
    float: read number of bytes.
    seek <list>: seek file.
    close: close file.
    verbose <float>: set verbosity on or off.
    creationmode <octal>: restrict permissions of the to-be-created file.
  2nd:
    symbol: change the associated file-handle.
outlets:
  1st:
    list: data bytes.
  2nd:
    bang: if file can't be opened, end of the file is reached or a read error occurred.
    seek <float>: seek output.

flags:
  -q: set quiet verbosity.
  -v: set loud verbosity.
  -m: file creation mode (user/group/other permissions) in octal.
  
methods:
  open <symbol> r: explicit Read-mode
  open <symbol> a: open file for writing (Append mode)
  open <symbol> c: open file for writing (Create (or trunCate) mode)
  
draft: false
pdcategory: Misc

---


The data you read from or write to a file are lists of bytes, which appear in Pd as lists of numbers from 0 to 255 (using out-of-range numbers of symbols leads to undefined behaviour.) The 2nd inlet of the 'file handle' object is documented in the 'file define' subpatch.