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
"""

#### --- verficar a lógica do exercício
print('Validador de CPF \n')

# validação da entrada fornecida

cpf = input('Digite um CPF: ')

if (cpf.isnumeric()) and (len(cpf) != 11):
    cpf = int(cpf)
    contador = 10
    soma = 0

    for digito in cpf:
        digito = cpf[contador]
        soma = soma + digito
        contador = -1

        if contador == 1:   # verificar isso depois
            break

   # cálculo do primeiro dígito

    digito1_valido = (soma * 10) % 11

    if (digito1_valido > 9):
        digito1_valido = 0

    print(f'O primeiro dígito do CPF é {digito1_valido}')
else:
    print('O CPF digitado não é válido.')