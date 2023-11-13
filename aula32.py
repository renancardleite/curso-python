"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um nuemro interio: ')

# if numero.isdigit():
#     numero_par = int(numero) % 2
#     if numero_par == 0:
#         print('Este número é par.')
#     else:
#         print('Este número é impar')
# else:
#     print('Este não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input('Digite o horário: ')
# primeiros_numeros = horario[0:2]

# if primeiros_numeros.isdigit():
#     hora = int(primeiros_numeros)
#     bom_dia = hora >= 0 and hora <= 11
#     boa_tarde = hora >= 12 and hora <= 17
#     boa_noite = hora >= 18 and hora <= 23

#     if bom_dia:
#         print('Bom dia!')
#     elif boa_tarde:
#         print('Boa tarde!')
#     elif boa_noite:
#         print('Boa noite!')
#     else:
#         print('Você não digitou um horário valido.')
# else:
#     print('Você não digitou um horário valido.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
quantidade_letras = len(nome)
curto = quantidade_letras <= 4
normal = quantidade_letras >= 5 and quantidade_letras <= 6
grande = quantidade_letras > 6

if curto:
    print('Seu nome é curto.')
elif normal:
    print('Seu nome é normal.')
elif grande:
    print('Seu nome é grande.')


