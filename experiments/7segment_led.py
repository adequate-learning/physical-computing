#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
# Switch off all the segments per digit
segments =  (11,4,23,8,7,10,18,25)
def init_segments():
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 1)

# Switch on GPIO ports that switch on off complete digits
digits = (22,27,17,24)
def init_digits():
    for digit in digits:
        GPIO.setup(digit, GPIO.OUT)
        GPIO.output(digit, 0)


num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
 
try:
    init_segments()
    init_digits()
    while True:
        s = '1337'
        for digit in range(4):
            for loop in range(7):
                d = s[digit]
                bit = num[d][loop]
                #print("digit: ", digit, " now setting pin: ", segments[loop], " for d: ", d, " bit: ", bit)

                GPIO.output(segments[loop], bit != 1)
                # control decimal point
                #if (bit == 0):
                #    GPIO.output(25, 1)
                #else:
                #    GPIO.output(25, 0)
            #print("grounding pin: ", digit)
            GPIO.output(digits[digit], 1)
            time.sleep(0.001)
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
finally:
    GPIO.cleanup()
