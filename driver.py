#!/usr/bin/env python3

import io
import time
import math
import servo

left_pin = 23 
right_pin = 24

right = servo.Servo(left_pin, invert=True)
left = servo.Servo(right_pin)

def drive(pitch, roll):
    # positive pitch for forward; positive roll for right
    right.setSpeed(pitch - roll)
    left.setSpeed(pitch + roll)

drive(0.5, 0.5)

time.sleep(1)

left.stop()
right.stop()
left.stopGpio()

