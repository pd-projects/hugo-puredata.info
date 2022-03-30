---
title: savepanel
description: query you for the name of a file to create.
categories:
- object
pdcategory: Misc
last_update: '0.48'
see_also:
- openpanel
- pdcontrol
inlets:
  1st:
    bang: open dialog window to choose a file name to save to.
    symbol: set starting directory and open dialog window.
outlets:
  1st:
    symbol: file name.
draft: false
---
When savepanel gets a "bang" a "Save As" file browser appears on the screen, If you choose a filename, it appears on the outlet.
