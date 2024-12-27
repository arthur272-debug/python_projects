# Combinations, Permutations e Product - Itertools
# Combinations - Ordem não importa - itrável + tamanho do grupo
# Permutations - Ordem importa
# Product - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterable):
    print(*list(iterable), sep='\n')
    print()

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
camisetas = [
             ['vermelha', 'verde', 'amarela'],
             ['P', 'M', 'G'],
             ['estampada', 'lisa'],
             ]

print('Combinations:')
print_iter(combinations(pessoas, 2))

print('Permutations:')
print_iter(permutations(pessoas, 2))

print('Product:')
print_iter(product(*camisetas))