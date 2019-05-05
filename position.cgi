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

a = int(arguments["a"].value)
b = int(arguments["b"].value)
g = int(arguments["g"].value)

pitch = ((90 + g) if (g < 0) else (90-g)) / 90
roll = b / 90

drive(pitch, roll)


