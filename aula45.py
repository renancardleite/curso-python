texto = 'Renan'
iterador = iter(texto)



while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in texto:
    print(letra)
