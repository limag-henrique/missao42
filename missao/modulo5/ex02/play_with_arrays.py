#!/usr/bin/python3
vetor = [2,8,5,9,4,5,61,65,65,65,65,9,4,2,8,61]
novo_vetor = []
print("Original: ", vetor)
i = 0
j = 0

while i < len(vetor):
    if vetor[i] > 5:
        novo_vetor.append(vetor[i]+2)
        i += 1
    else:
        i += 1

print("Modificado: ", novo_vetor)
