# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar_variavel(*args):
    total = 1
    for argumento in args:
        total *= argumento
    return total


somatorio = multiplicar_variavel(1, 2, 3, 4, 5)
print(somatorio)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def verificar_numero(numero):
    numero_par = numero % 2 == 0

    if numero_par:
        return f"{numero} é par."
    return f"{numero} não é par."


print(verificar_numero(2))
print(verificar_numero(5))
print(verificar_numero(8))
print(verificar_numero(9))
