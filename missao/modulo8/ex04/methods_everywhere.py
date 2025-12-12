#!/usr/bin/python3

import sys

def shrink(argumento):
    i = 0
    print(argumento[:8])
        
def enlarge(argumento):
    vetor_de_z = ""
    impressoes_restantes = 8 - len(argumento)
    while impressoes_restantes > 0:
        vetor_de_z += "Z"
        impressoes_restantes -= 1
    return vetor_de_z

if len(sys.argv) < 2:
    print("none")
else: 
    j = 1
    while j < len(sys.argv):
        if (len(sys.argv[j]) > 8):
            shrink(sys.argv[j])
        elif (len(sys.argv[j]) == 8):
            print(sys.argv[j])
        else:
            print(f"{sys.argv[j]}{enlarge(sys.argv[j])}")
        j += 1

# fatiar : print(0:8), que imprime a lista do 0º ao 8º termo

