# Exercício -> Unir Listas  - depois subir o exercício no git
# Realizar através da função zipper
from itertools import zip_longest


def zipper(lista1, lista2):
    indice_menor = min(len(lista1), len(lista2))
    lista_unida = [(lista1[i], lista2[i]) for i in range(indice_menor)]
    return lista_unida

# print(zipper(lista_a, lista_b))


# como que 'funciona' a função "zip" por trás dos panos
lista_a = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_b = ['BA', 'SP', 'MG', 'RJ']


# A função propriamente dita
lista_nova = list(zip(lista_a, lista_b))  # pega o índice da menor lista
print(lista_nova)


lista_nova_invertida = list(zip_longest(
    lista_a, lista_b, fillvalue='Sem cidade'))  # pega o índice da maior lista
print(lista_nova_invertida)
