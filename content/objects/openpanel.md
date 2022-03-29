---
title: openpanel
description: query for files or directories.
categories:
- object
last_update: '0.51'
see_also:
- savepanel
- pdcontrol
inlets:
  1st: 
    bang: "open dialog window to choose file(s) or directory."	
    symbol: set starting directory and open dialog window.
outlets:
  1st:
    symbol: "directory or file(s)' names."
arguments:
  float: "mode: 0 (file, default), 1 (directory), 2 (multiple files)."

draft: false
pdcategory: Misc

---

When openpanel gets a "bang", a file browser appears on the screen. By default, if you select a file, its name appears on the outlet.

A mode argument allow you to select a directory or multiple files.
