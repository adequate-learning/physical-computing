#!/usr/bin/env python

import colorsys
import math
import time

import pantilthat


pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)

r, g, b, w = 0, 0, 0, 50

while True:
    pantilthat.brightness(128)
    for x in range(8):
        pantilthat.set_pixel(x, 0, 0, 255)

    pantilthat.show()
    time.sleep(0.1)

    #    pantilthat.set_pixel(x, r, g, b, w)
    #pantilthat.set_pixel(0, 255, 0, 255)

    #p = int(math.sin(time.time()) * 90)
    #t = int(math.sin(time.time()) * 90)
    #print("pan: ", p)
    #print("tilt: ", t)
#    pantilthat.pan(p)
#    pantilthat.tilt(t)
