lista = [10, 20, 30, 40, 50 , 60]
lista[2] = 300
print(lista)
print(lista[2])

del lista[2]
print(lista)
print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido, ', ultimo_valor)

