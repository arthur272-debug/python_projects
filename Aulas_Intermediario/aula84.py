# Aula sobre Generator expression, Iterables e Iterators em Python - Parte 2

import sys

lista = [n for n in range(10000)]
generator2 = (n for n in range(10000))

print(lista)
print(sys.getsizeof(lista))  # tamanho armazenado na memória

print(generator2)
print(sys.getsizeof(generator2))  # tamanho armazenado na memória
