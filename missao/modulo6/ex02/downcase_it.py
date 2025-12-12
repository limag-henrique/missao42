#!/usr/bin/python3
import sys

if len(sys.argv) == 2:
    small = sys.argv[1]
    print(small.lower())
else:
    print("none")