string = 'ABDC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a, b, c, *_, c= lista
# print(a, c)

# for nome in lista:
#     print(nome, end=' ', sep='')
try:
    print(*lista)
    print(*string)
    print(*tupla)
except:
    ...