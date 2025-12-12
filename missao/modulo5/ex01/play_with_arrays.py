#!/usr/bin/python3
vetor = [2,8,5,9,4,5,61,65]
print("Original: ", vetor)
i = 0

while i < len(vetor):
    vetor[i] = vetor[i]+2
    i += 1

print("Modificado: ", vetor)
