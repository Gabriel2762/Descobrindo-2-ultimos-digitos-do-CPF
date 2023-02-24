import os

print('DESCOBRINDO OS DIGITOS DO CPF')

while True:
    cpf = input('Digite apenas os 9 primeiros números do seu cpf: ')
    if cpf.isnumeric():
        ...
        
        if len(cpf) > 9: 
            print('Digite apenas 9 números')
            continue

        elif len(cpf) < 9:
            print('Digite 9 números')
            continue
        
    else:
        print('Digite apenas números')
        continue

    os.system('cls')
    cpf_novo=''
    nove_digitos = cpf[:9]

    contador_regressivo_1 = 10
    contador_regressivo_2 = 11

    resultado_digito_1 = 0
    resultado_digito_2 = 0

    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10 % 11)
    digito_1 = digito_1 if digito_1 <=9 else 0
    cpf_novo = cpf + str(digito_1)



    dez_digitos = cpf_novo[:10]
    cpf_novo_1 =''
    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
        
    digito_2 = (resultado_digito_2 * 10 % 11)
    digito_2 = digito_2 if digito_2 <=9 else 0

    cpf_novo_1 = cpf_novo + str(digito_2)
    print('O seu CPF é:', cpf_novo_1)
    break