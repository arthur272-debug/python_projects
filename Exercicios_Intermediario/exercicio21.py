""" - terminar de assistir o vídeo
Enunciado

Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

===================== resultado
lista_soma = [2,4,6,8]
"""


def somar_listas(lista1, lista2):
    intervalo_menor = min(len(lista1), len(lista2))
    resultado = (lista1[i]+lista2[i] for i in range(intervalo_menor))
    return resultado


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


lista_soma = somar_listas(lista_a, lista_b)
print(f'lista soma = {list(lista_soma)}')
