nome = 'Renan'
peso = 99
altura = 1.79
imc = peso / (altura * altura) #IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura:,.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
#Renan tem 1.79 de altura,
#pesa 95 quilos e seu IMC é
#IMC