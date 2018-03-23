#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

TRIG = 23 
ECHO = 24

def ping():
    GPIO.setmode(GPIO.BCM)
    print "Distance Measurement In Progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = 0
    pulse_end = 0

    print("waiting until echo becomes 1")
    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    print("waiting until echo becomes 0")
    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    print("Duration: ", pulse_duration)
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Distance:",distance,"cm"
    GPIO.cleanup()



try: 
  while True: 
    ping()
    time.sleep(2)

except KeyboardInterrupt:
    print "Done..."
finally:
    GPIO.cleanup()
