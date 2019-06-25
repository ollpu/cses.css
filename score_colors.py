#!/usr/bin/env python3

import sys, math, struct

if len(sys.argv) > 1:
    k = float(sys.argv[1])
else:
    k = 0.6

if len(sys.argv) > 2 and sys.argv[2] == 'dark':
    # TODO
    mult, offs = 0.696, 0.189
else:
    mult, offs = 0.696, 0.189

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
