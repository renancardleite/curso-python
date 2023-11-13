# pessoa = {
#     'nome': 'Renan',
#     'sobrenome': 'Rafael',
#     'idade': 34
#  }

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# pessoa.setdefault('idade', None)
# print(pessoa['idade'])


# for chave in pessoa.values():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# d2 = d1.copy()
# d2 = copy.copy(d1)
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 5555

print(d1)
print(d2)
