# Aprendendo sobre reduce 

from functools import reduce

produto =[
    {'nome': 'Produto 1', 'preco': 13},
    {'nome': 'Produto 2', 'preco': 55},
    {'nome': 'Produto 3', 'preco': 5},
    {'nome': 'Produto 4', 'preco': 22},
    {'nome': 'Produto 5', 'preco': 100},
]

total = reduce(lambda acumulador,p: p['preco']+ acumulador,produto,0)
print(f'Preço total: R${total}')