

while True:
    cpf = input('Digite os 9 primeiros numero do CPF (apenas numeros): ')
    tam_cpf = len(cpf) == 9

    if tam_cpf is False:
        print('Digite um CPF valido')
        continue

    else:

        dig_1 = int(cpf[0]) * 10    
        dig_2 = int(cpf[1]) * 9
        dig_3 = int(cpf[2]) * 8
        dig_4 = int(cpf[3]) * 7
        dig_5 = int(cpf[4]) * 6
        dig_6 = int(cpf[5]) * 5
        dig_7 = int(cpf[6]) * 4
        dig_8 = int(cpf[7]) * 3
        dig_9 = int(cpf[8]) * 2

        sum_dig = (dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 + dig_7 + dig_8 + dig_9) * 10

        res_sum_dig = sum_dig % 11
        # print(res_sum_dig)

        if res_sum_dig < 10:
            print(f'O primeiro número do digito do CPF é {res_sum_dig}')
        
        else:
            print('O primeiro número do digito do CPF é 0')


