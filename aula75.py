def multiplica(numero):
    def multiplicar(fator):
        return numero * fator
    return multiplicar

duplicar = multiplica(2)
triplicar = multiplica(3)
quadruplica = multiplica(4)

print(duplicar(1))
print(triplicar(1))
print(quadruplica(1))