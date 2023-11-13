nome = 'Pamela Comparoni'

tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
print(nome[11])

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    print(novo_nome)
    indice += 1

print(novo_nome)