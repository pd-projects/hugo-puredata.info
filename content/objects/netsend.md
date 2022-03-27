---
title: netsend
description: send Pd messages over a network
categories:
- object
last_update: '0.51'
inlets:
  1st:
    connect <list>: sets host and port number, an additional port argument can be set for messages sent back from the receiver.
    disconnect: close the connection.
    timeout <float>: TCP connect timeout in ms (default 10000).
    send <anything>: sends messages over the network.
    list: works like 'send'.
    
outlets:
  1st:
    float: nonzero if connection is open, zero otherwise.
  2nd:
    anything: messages sent back from netreceive objects.
flags:
  -u: sets UDP connection (default TCP).
  -b: sets to binary mode (default 'FUDI').
draft: false
pdcategory: Misc

---

As of 0.51, Pd supports IPv6 addresses, netsend -u (UDP) is fully "connectionless" and no longer closes if no one receives a UDP message, and netsend (TCP) has a settable connect timeout which defaults to 10 seconds.

The netsend object sends TCP ("stream") or UDP ("datagram") messages over the network, which can be received by netreceive objects in other patches (which may be running on another machine). An outlet reports whether the connection is open or not. A connection request should specify the name or IP address of the other host and the port number. There should be a "netreceive" on the remote host with a matching port number.

By default the messages are ASCII text messages compatible with Pd (i.e., numbers and symbols terminated with a semicolon -- the "FUDI" protocol). The "-b" creation argument specifies binary messages instead, which appear in Pd as lists of numbers from 0 to 255 (You could use this to send OSC messages, for example.)

The Pd distribution includes "pdsend" and "pdreceive" standalone programs that work with netsend/netreceive in FUDI mode.

First outlet is nonzero if connection is open, zero otherwise.

Second outlet outputs messages sent back from netreceive object. In TCP mode this works for any established connection. In UDP you have to send at least one message forward through the connection for backward messages to find their way back.

An old (pre-0.45) calling convention is provided for compatibility: a single float argument, "0" or "1" for TCP or UDP respectively.

