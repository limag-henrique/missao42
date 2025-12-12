#!/usr/bin/python3

def average(alunos):
    i = 0
    lista = list(alunos.values())
    numeros = 0

    while i < len(lista):
        numeros += lista[i]
        i += 1

    return(numeros/len(lista))

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")




    


