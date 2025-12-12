#!/usr/bin/python3
vetor = [2, 8, 9, 48, 8, 22, -12, 2]
novo_vetor = []
print("Original: ", vetor)
i = 0
j = 0

while i < len(vetor):
    if vetor[i] > 5:
        novo_vetor.append(vetor[i]+2)    
    i += 1

print("Modificado: ", set(novo_vetor))
