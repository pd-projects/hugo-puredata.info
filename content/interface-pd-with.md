---
title: "Interface Pd with"

draft: false
---

# Interface Pd with 

For an overview of on "how to install externals" see [externals](../externals).

### Ableton Link

You can use the {{< deken "abl_link~" >}} external.


### Arduino

You can use the {{< deken "pduino" >}} external.


### Art-Net

You can use the {{< deken "artnetlib" >}} external.


### Comport

You can use the {{< deken "comport" >}} external.

### HID

You can use several externals:

  - {{< deken "hid" >}} (Linux, macOS)
  - {{< deken "hidin" >}} (MS-Windows)
  - {{< deken "hidio" >}} (MS-Windows)
  - {{< deken "hidraw" >}} (Linux, macOS, MS-Windows)

### Icecast/Shoutcast

You can use the {{< deken "mp3cast~" >}} external.

### JSON

You can use the {{< deken "purest_json" >}} external.

### LUA

You can use the {{< deken "pdlua" >}} external.

### MIDI

See built-in objects in [I/O via MIDI, OSC, and FUDI]({{< mdlink "../objects" "I/O via MIDI, OSC, and FUDI">}})

### OSC

See built-in objects in [I/O via MIDI, OSC, and FUDI]({{< mdlink "../objects" "I/O via MIDI, OSC, and FUDI">}})

### (raw) TCP/IP

See built-in objects [[netsend]](../objects/netsend/) [[netreceive]](../objects/netreceive/)


### (raw) UDP

See built-in objects [[netsend]](../objects/netsend/) [[netreceive]](../objects/netreceive/)


### VST

To load vst plugins inside Pd:

  - use the {{< deken "vstplugin~" >}} external.
  
To run Pd inside a vst host:

  - [plugdata](https://plugdata.org/)
  
  - [camomile](https://github.com/pierreguillot/Camomile)
  
  - [pdvst](https://git.nubegris.com.ar/lucarda/pdvst-0.52/releases) (MS-Windows only)

### WebSocket

You can use externals:

  - {{< deken "ws" >}}
  - {{< deken "websocketserver" >}}

