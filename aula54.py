lista = []

while True:
    print('Selcione uma opção')
    opcoes =  input ('[i]nserir [a]apagar [l]istar: ')
    valores_permitidos = ('i,a,l')
    
    if opcoes not in valores_permitidos:
        print('Opção invalida, favor selecionar uma opção valida')
        continue

    if opcoes == 'i':
        itens = input('Inserir um Item: ')
        itens
        lista.append(itens)
        continue

    if opcoes == 'l':
        
        if len(lista) == 0:
            print('Lista vazia, favor incluir itens para serem mostrados.')
            continue

        for indice, item in enumerate (lista):
            print(indice, item)

    if opcoes == 'a':
        apagar = int(input ('inserir o número do Item que deseja apagar: '))
        indices = len(lista)

        if apagar >= indices:
            print('Item inexistente, selecione a opção [l]istar para consultar os itens existentes.')
            continue

        del lista[apagar]


