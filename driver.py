#!/usr/bin/env python3

import servo
import sys
import re
import math
import time

left_pin = 23
right_pin = 24

right = servo.Servo(left_pin, invert=True)
left = servo.Servo(right_pin)

def drive(a, direction, g):
    rs = math.cos(direction+45)
    ls = math.cos(direction-45)
    print('rs %d ls %d' % (rs, ls))
    right.setSpeed(rs)
    left.setSpeed(ls)
    time.sleep(0.15)
    left.setSpeed(0)
    right.setSpeed(0)

try:
    for line in sys.stdin:
        m = re.match(r'a=([-]?\d+)&b=([-]?\d+)&g=([-]?\d+)', line)
        if (m):
            v = m.groups()
            drive(int(v[0]), int(v[1]), int(v[2]))
except:
    left.stop()
    right.stop()
    left.stopGpio()

