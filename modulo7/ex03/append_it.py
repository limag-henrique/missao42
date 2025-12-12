#!/usr/bin/python3
import sys

tamanho = len(sys.argv)

if tamanho < 2:
    print("none")
else:
    i = 1

    while i < (tamanho):
        if (sys.argv[i].find("ism", len(sys.argv[i])-3)) != -1:
            i += 1    
        else:
            print(f"{sys.argv[i]}ism")
            i += 1

