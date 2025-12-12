#!/usr/bin/python3
import sys

def downcase_it():
    if len(sys.argv) < 2:
        print("none")
    else:
        i = 1
        while i < len(sys.argv):
            print(sys.argv[i].lower())
            i += 1

downcase_it()





