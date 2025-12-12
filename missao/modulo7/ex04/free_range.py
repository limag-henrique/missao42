#!/usr/bin/python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    min = int(sys.argv[1])
    max = int(sys.argv[2])
    vetor = []

    while min <= max:
        vetor.append(min)
        min += 1
    print(vetor)