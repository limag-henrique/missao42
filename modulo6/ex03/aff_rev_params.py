#!/usr/bin/python3
import sys

if len(sys.argv) <= 2:
    print("none")
else:
    tamanho = 1
    while (tamanho <= (len(sys.argv))):
        print(sys.argv[len(sys.argv)-tamanho])
        tamanho = tamanho + 1
