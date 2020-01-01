#!/usr/bin/env python3

# Generates hex color codes for a ramp in score -- 0 is red, 50 is yellowish,
# 100 is green

import sys, math, struct

if len(sys.argv) > 1:
    k = float(sys.argv[1])
else:
    k = 0.6

# These values are extracted from the base colors.
# e.g. a red #f07c7c corresponds to 0xf0, 0x7c
hex_ref = [0xf0, 0x7c]

if len(sys.argv) > 2 and sys.argv[2] == 'dark':
    # Same colors for now
    pass

hl, bl = [(x/255)**2 for x in hex_ref]
mult, offs = hl-bl, bl


for s in range(0, 101):
    x = s / 100
    c = None
    if x < 0.5:
        c = [1, math.pow(2*x, k), 0]
    else:
        c = [math.pow(2-2*x, k), 1, 0]
    c = [offs+v*mult for v in c]
    c = [round(math.sqrt(v)*255) for v in c]
    c = "#{0:02x}{1:02x}{2:02x}".format(*c)
    print(s, c)
