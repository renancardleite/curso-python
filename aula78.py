# s1 = set() vazio
# s1 = {'Luiz', 1, 2, 3} # set com dados
# print(s1, type(s1))

# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3, 3, 3, 3, 1}

# s1 = set('Luiz')

# s1 = s1 = {1, 2, 3}

# # print(3 not in s1)

# for numero in s1:
#     print(numero)

s1 = set()
s1.add ('Luiz')
s1.add (1)
s1.update(('Olá Mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá Mundo')
# print(s1)

s1 = {1, 2, 3}
print (s1)
s2 = {2, 3, 4}
print(s2)
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print(s3)
print(s4)
print(s5)
print(s6)


