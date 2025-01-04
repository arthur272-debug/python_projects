# aula sobre map e partial

from functools import partial

produtos =[
    {'nome': 'Produto 2', 'preco': 50.50},
    {'nome': 'Produto 3', 'preco': 20.10},
    {'nome': 'Produto 4', 'preco': 30.70},
    {'nome': 'Produto 5', 'preco': 70.28},
    {'nome': 'Produto 1', 'preco': 80.95},
]

def aumentarPorcentagem(valor, porcentagem):
    return round (valor * porcentagem, 2)

aumentar_30_porcento = partial(aumentarPorcentagem, porcentagem=1.3)

def aumentarProduto_porcentagem(produto):
    return {**produto, 'preco': aumentar_30_porcento(produto['preco'])}

novos_produtos = map(aumentarProduto_porcentagem, produtos)

print('Produtos com preços originais:')
print(list(produtos))
print('\nProdutos com 30% de aumento:')
print(list(novos_produtos))