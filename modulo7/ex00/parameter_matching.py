#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    parametro = input("Qual que é a senha? ")
    if sys.argv[1] == parametro:
        print("Parabéns!")
    else:
        print("Não... foi mal")






