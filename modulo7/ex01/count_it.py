#!/usr/bin/python3
import sys

tamain = len(sys.argv)

if tamain < 2:
    print("none")
else:
    print(f"Parâmetro(s): {tamain-1}")

    for numero in range(1,tamain):
        print(f"{sys.argv[numero]}: {len(sys.argv[numero])}")