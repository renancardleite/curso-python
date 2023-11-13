# x, y, *resto = 1, 2, 3, 4

# print(x, y, resto)

# def soma (x, y):
#     return x + y

def soma(*args):
    # args = list(args)
    # print(args)
    total = 0
    for numero in args:
        # print('Total', total, numero)
        total += numero
        # print('Total', total)

    return total

    # print(total)

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

print(sum((1, 2, 3, 4, 5, 78, 65), (50000)))