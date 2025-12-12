#!/usr/bin/python3

def array_de_nomes(pessoas):
    primeiro_nome = list(pessoas)
    sobrenome = list(pessoas.values())

    i = 0
    lista = []

    while i < len(pessoas):
        first_maiuscula = primeiro_nome[i].capitalize()
        sobrenome_maiuscula = sobrenome[i].capitalize()
        lista.append(first_maiuscula + " " + sobrenome_maiuscula)
        i += 1
    
    return lista

pessoas = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_de_nomes(pessoas))