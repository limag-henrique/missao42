#!/usr/bin/python3

def get_birth_year(cientista):
    return int(cientista["date_of_birth"])

def ordenar_por_ano(lista):
    n = len(lista)
    trocou = True

    while trocou:
        trocou = False
        i = 0
        while i < n - 1:
            if get_birth_year(lista[i]) > get_birth_year(lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True
            i += 1
        n -= 1

    return lista

def famous_births(mulheres_fodas):
    lista_cientistas = list(mulheres_fodas.values())

    lista_cientistas = ordenar_por_ano(lista_cientistas)

    i = 0
    while i < len(lista_cientistas):
        posicao = lista_cientistas[i]
        nome = posicao['name']
        ano = posicao['date_of_birth']
        print(f"{nome} is a great scientist born in {ano}")
        i += 1 


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)


# #!/usr/bin/python3

# def famous_births(mulheres_fodas):
#     lista_ordenada = sorted(mulheres_fodas.values(), key=lambda cientista_fodona: cientista_fodona['date_of_birth'])

#     i = 0
#     while i < len(lista_ordenada):
#         scientist = lista_ordenada[i]
#         nome = scientist['name']
#         ano = scientist['date_of_birth']
        
#         print(f"{nome} is a great scientist born in {ano}")
#         i += 1

# women_scientists = {
#     "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
#     "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
#     "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
#     "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
# }

# famous_births(women_scientists)


# Devo deixar em ordem cronológica a impressão dos nomes das cientistas. Faça as modificações necessárias para que o código funcione corretamente. Não use key=lambda, use funções simples
# #!/usr/bin/python3
# def famous_births(mulheres_fodas):
#     lista_cientistas = list(mulheres_fodas.values())
    
#     i = 0
#     while i < len(lista_cientistas):
#         posicao = lista_cientistas[i]
#         nome = posicao['name']
#         ano = posicao['date_of_birth']
#         print(f"{nome} is a great scientist born in {ano}")
#         i += 1 

# women_scientists = {#!/usr/bin/python3

# Função auxiliar para obter o ano de nascimento
# def get_birth_year(cientista):
#     return int(cientista["date_of_birth"])

# # Função de ordenação manual (bubble sort usando while)
# def ordenar_por_ano(lista):
#     n = len(lista)
#     trocou = True

#     while trocou:
#         trocou = False
#         i = 0
#         while i < n - 1:
#             if get_birth_year(lista[i]) > get_birth_year(lista[i + 1]):
#                 lista[i], lista[i + 1] = lista[i + 1], lista[i]
#                 trocou = True
#             i += 1
#         n -= 1

#     return lista

# def famous_births(mulheres_fodas):
#     lista_cientistas = list(mulheres_fodas.values())

#     # Ordenar sem lambda, usando a função acima
#     lista_cientistas = ordenar_por_ano(lista_cientistas)

#     i = 0
#     while i < len(lista_cientistas):
#         posicao = lista_cientistas[i]
#         nome = posicao['name']
#         ano = posicao['date_of_birth']
#         print(f"{nome} is a great scientist born in {ano}")
#         i += 1 


# women_scientists = {
#     "ada":    { "name": "Ada Lovelace", "date_of_birth": "1815" },
#     "cecilia":{ "name": "Cecila Payne", "date_of_birth": "1900" },
#     "lise":   { "name": "Lise Meitner", "date_of_birth": "1878" },
#     "grace":  { "name": "Grace Hopper", "date_of_birth": "1906" }
# }

# famous_births(women_scientists)







