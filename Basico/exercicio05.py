"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero_str)
    numero_par = numero_inteiro % 2 == 0
    
    if (numero_par):
        print('O número digitado é par.')
    else:
        print('O número digitado é ímpar.')
except:
    print('O número digitado em questão não é do tipo inteiro!!')