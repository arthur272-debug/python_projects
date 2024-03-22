import random

print('Gerador de CPF \n')

cpf = ''

# Gerando números aleatórios

for i in range(9):
    cpf += str(random.randint(0, 9))

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

cpf = cpf + str(digito1_valido)

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

cpf = cpf + str(digito2_valido)

print(f'CPF: {cpf}')
