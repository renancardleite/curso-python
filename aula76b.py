p1 = {
    'nome': 'Renan',
    'sobrenome': 'Rafael',
    # 'idade': 34,
 }

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 34
# })

# p1.update(nome='novo valor', idade=34)

# tupla = (('nome', 'novo valor'), ('idade', 34))
lista = [['nome', 'novo valor'], ['idade', 34]]
p1.update(lista)
print(p1)