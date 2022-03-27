---
title: garray
description: graphical array (messages received via array name).
categories:
- object
last_update: '0.52'
see_also:
- inlet
- namecanvas
- array
methods:
  list: sets values into array, fisty element is starting index (from 0).
  const <float>: optional float sets a constant value to all indexes (default 0).
  resize <float>: resizes the array.
  sinesum <list>: first element sets array size, remaining elements set amplitude of sine components.
  cosinesum <list>: first element sets array size, remaining elements set amplitude of cosine components.
  print: prints array information (name, type, size) on the terminal window.
  normalize <float>: normalizes to maximum absolute amplitude set by optional float (default 1).
  read <symbol>: load contents from a text file with the symbol name.
  write <symbol>: save contents to a text file with the symbol name.
  rename <symbol>: renames the array to a new name defined by the given symbol.
  bounds <list>: sets rectangle bounds (xmin, ymax, xmax, ymin).
  xticks <list>: sets a point to put a tick, the interval between ticks, and the number of ticks overall per large tick.
  yticks <list>: same as above for the 'y' axis.
  xlabels <list>: first element is a label offset, remaining are the values to label.
  ylabels <list>: first element is a label offset, remaining are the values to label.
  vis <float>: zero hides array, non zero shows it.
  width <float>: sets array's width (default 1).
  color <float>: sets array color in the same format as Data Structures.
  style <float>: sets display style (0-point, 1-polygon, 2-bezier).
  edit <float>: non zero allows editing with the mouse, zero prevents it.

draft: false
pdcategory: Arrays & Tables

---

Input is via send names
