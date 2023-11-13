lista = ['Maria', 'Helena', 'Luiz']
lista.append('Renan')

# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)

# for lista_num in lista_enumerada:
#     print(lista_num)

# print('O que tem na lista enumerada: ', lista_enumerada)

# for lista_num in lista_enumerada:
#     print(lista_num)

for indice, nome in enumerate(lista):
    print(indice, nome)
