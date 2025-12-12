#!usr/bin/python3
numero = input("Insira um numero: ")
num = float(numero) % 1

if num == 0:
    print("É um número inteiro")
else:
    print("É um número decimal")