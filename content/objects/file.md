---
title: file
description: low-level file operations
categories:
- object
pdcategory: Misc
last_update: '0.52'
see_also:
- text
- array
- list
- file handle
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
arguments:
- type: symbol
  description: 'sets the function of [file], possible values: handle, define, mkdir,
    which, glob, stat, isfile, isdirectory, size, copy, move, delete, split, join,
    splitext and splitname. The default value is ''handle''.'
flags:
- flag: -q
  description: set quiet verbosity.
- flag: -v
  description: set loud verbosity.
- flag: -m
  description: file creation mode (user/group/other permissions) in octal.
inlets:
  1st:
    close: close file.
    creationmode <octal>: restrict permissions of the to-be-created file.
    float: read number of bytes.
    open <symbol>: open a file.
    seek <list>: seek file.
    verbose <float>: set verbosity on or off.
  2nd:
    symbol: change the associated file-handle.
outlets:
  1st:
    list: data bytes.
  2nd:
    bang: if file can't be opened, end of the file is reached or a read error occurred.
    seek <float>: seek output.
methods:
- method: open <symbol> r
  description: explicit Read-mode
- method: open <symbol> a
  description: open file for writing (Append mode)
- method: open <symbol> c
  description: open file for writing (Create (or trunCate) mode)
draft: false
---
Short for "file handle"
