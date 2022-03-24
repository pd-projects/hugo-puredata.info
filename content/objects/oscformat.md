---
title: "[oscformat]"
description: "OSC messages to and from Pd lists"
bref: "OSC messages to and from Pd lists"
draft: false
categories: ["object"]
pdcategory: "I/O via MIDI, OSC, and FUDI"
---

### [oscformat]

OSC messages to and from Pd lists.

Oscformat makes OSC (Open Sound Control) packets (byte by byte) suitable for sending over the network via netsend (in UDP binary mode). The OSC address (the strings between the slashes) are given by the creation arguments or by "set" messages. Oscparse takes lists of numbers interpreting them as the bytes in an OSC message and outputs a list containing, first, the symbols making up the address of the OSC packet, and following that, numbers and symbols as present in the OSC message.

If a format is given (via the '-f' flag or 'format' message) oscformat interprets incoming data as integer, float, string, or 'blob'. Blobs are given as an atom count followed by that number of elements. (If an elements is a symbol, its first byte is sent). If the count is negative, the entire remaining message is included in the blob (but the OSC parser will report the actual number of elements). If the elements aren't exhausted at the end of the format string, the default (float and symbol) conversions are made for the rest.

Note: there's no way using oscparse to distinguish between floats and integers, nor to see blobs unambiguously. OSC messages may be combined in "bundles". If oscparse receives a bundle it simply parses all the messages in the bundle in the order they appear, and ignores the bundle's time tag.

INLET:

- list - list to format into a OSC packet.

- set &lt;list&gt; - set one or more adresses.

- format &lt;symbol&gt; - characters set format types: 'b' (blob),  'i' (interger),  'f' (float) or 's' (sring).

OUTLET:

- list - converted OSC packet from lists.

ARGUMENTS:

- flag:

  - -f &lt;symbol&gt;: sets format as in the 'format' message

- args:

  - list - list of one or more addresses
  
> see also [[oscparse]](../oscparse) [[fudiformat]](../fudiformat) [[netsend]](../netsend) [[list]](../list) 
 
> updated for Pd version 0.51.
 
