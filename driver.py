#!/usr/bin/env python3

import servo
import sys
import re

left_pin = 23
right_pin = 24

right = servo.Servo(left_pin, invert=True)
left = servo.Servo(right_pin)

def drive(pitch, roll):
    # positive pitch for forward; positive roll for right
    rs = pitch - roll
    ls = pitch + roll
    right.setSpeed(rs)
    left.setSpeed(ls)

def drive_orientation(a, b, g):
    pitch = ((g + 90) if (g < 0) else (g - 90)) / 90
    roll = b / 90
    drive(pitch, roll)

try:
    for line in sys.stdin:
        m = re.match(r'a=([-]?\d+)&b=([-]?\d+)&g=([-]?\d+)', line)
        if (m):
            v = m.groups()
            drive_orientation(int(v[0]), int(v[1]), int(v[2])) 
except:
    left.stop()
    right.stop()
    left.stopGpio()

