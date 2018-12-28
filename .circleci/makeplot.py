#!/usr/bin/env python

import argparse
p = argparse.ArgumentParser()
p.add_argument("plotid", type=int, choices=range(1, 5))
args = p.parse_args()

with open("myplot.txt", "w") as f:
  f.write("I am plot #{}!".format(args.plotid))
