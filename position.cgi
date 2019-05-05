#!/usr/bin/env python3

import cgi
import servo

arguments = cgi.FieldStorage()

left_pin = 23
right_pin = 24

right = servo.Servo(left_pin, invert=True)
left = servo.Servo(right_pin)

def drive(pitch, roll):
    # positive pitch for forward; positive roll for right
    right.setSpeed(pitch - roll)
    left.setSpeed(pitch + roll)

a = arguments["a"].value
b = arguments["b"].value
g = arguments["g"].value

#drive(0.5, 0.5)


