def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao
# print(saudacao('Bom dia'))
# v = saudacao('Bom dia')
# print(v)
# print(saudacao_2)
v = executa(saudacao, 'Bom dia', "Renan")
print(v)

