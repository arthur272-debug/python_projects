# aula sobre args - argumentos não nomeados

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma1 = soma(1, 2, 3, 4)
print(soma1)

soma3 = soma(4, 5, 6)
print(soma3)

numeros = 1, 2, 3, 4, 5, 6
outra_soma = soma(*numeros)
print(outra_soma)
