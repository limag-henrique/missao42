#!/usr/bin/python3
import sys
import re

if len(sys.argv) > 3:
    print("none")
elif len(sys.argv) < 3:
    print("none")
elif(len(re.findall(sys.argv[1], sys.argv[2]))) == 0:
    print("none")
else:
    quantidade = re.findall(sys.argv[1], sys.argv[2])
    print(len(quantidade))







