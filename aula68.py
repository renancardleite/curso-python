x = 1
y = 2


def escopo ():
    # global x
    x = 10
    def outra_funcao():
        x = 30
        y = 20
        print(x, y)
    outra_funcao() 
    # print(x, y)


escopo()

# print(x, y)