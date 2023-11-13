# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

#Avaliação de curto circuito
print(True and 0 and True)
print(bool(' '))

if 0 and 1:
    print(True and 1)