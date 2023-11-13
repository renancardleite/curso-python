def multplicar(*args):
    
    total = 1
    for numero in args:        
        # total = numero * total
        total *= numero
    # print(total)
    return total

multiplicacao = multplicar(2, 2, 10, 50, 80, 1000)
print(multiplicacao)
print(2*2*10*50*80*1000)

# ****************************

def epar(x):
    numero = x % 2
    if numero == 0:
        print('Este numero é par')
    else:
        print('Este numero é impar')

epar(100)

# solução professor

def par_impar (numero):
    multiplo_de_dois = numero % 2 ==0

    if multiplo_de_dois:
        return f'{numero} é Par'
    return f'{numero} é Impar'
    
print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))
