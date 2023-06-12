"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app

This example shows how to use advanced functions of Blynk library:
- insecure connection
- debug logging
- custom server
- changing heartbeat
- connected/disconnected events
- generic virtual pin events
"""

from __future__ import print_function
import BlynkLib

BLYNK_AUTH = 'YourAuthToken'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH,
                       insecure=True,          # disable SSL/TLS
                       server='blynk.cloud',   # set server address
                       port=80,                # set server port
                       heartbeat=30,           # set heartbeat to 30 secs
                       log=print               # use print function for debug logging
                       )

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

@blynk.on("V*")
def blynk_handle_vpins(pin, value):
    print("V{} value: {}".format(pin, value))

while True:
    blynk.run()
