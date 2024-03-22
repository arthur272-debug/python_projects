"""
Calculo do primeiro dígito do CPF 
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""

print('Validador de CPF \n')

# validação da entrada fornecida

cpf = input('Digite um CPF: ')

if (cpf.isnumeric()) and (len(cpf) == 11):
    multiplicador = 10
    soma = 0
# cálculo do primeiro dígito

    for digito_01 in cpf:
        digito_01 = int(digito_01)
        conta = digito_01 * multiplicador
        soma = soma + conta
        multiplicador -= 1

        if multiplicador == 1:
            break

    digito1_valido = (soma * 10) % 11
    digito1_valido = digito1_valido if digito1_valido <= 9 else 0

# cálculo do segundo dígito
    soma = 0
    multiplicador = 11
    for digito_02 in cpf:

        digito_02 = int(digito_02)
        conta = digito_02 * multiplicador
        soma = soma + conta
        if multiplicador == 2:
            break

        multiplicador -= 1

    digito2_valido = (soma * 10) % 11
    digito2_valido = digito2_valido if digito2_valido <= 9 else 0

    if (digito1_valido == int(cpf[9])) and (digito2_valido == int(cpf[10])):
        print(f'O CPF {cpf} é válido!')
    else:
        print(f'O CPF {cpf} não é válido!')

else:
    print('O CPF digitado não é válido.')
