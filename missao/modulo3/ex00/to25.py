#!/usr/bin/python3
numero = int(input("Enter a number less than 25\n"))

if (numero>=25):
    print("SABE LER NÃO? EU DISSE MENOR QUE 25, sô! Encerrando...")
else:
    while(numero <= 25):
        print(f"Inside the loop, my variable is {numero}")
        numero = numero + 1
