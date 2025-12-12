#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("none")

else:
    parametro = sys.argv[1]
    impressao = ""

    for i in range(0,len(parametro)):
        if parametro[i] == 'z':
            impressao += parametro[i]

    if impressao == "":
        print("none")
    else:
        print(impressao)