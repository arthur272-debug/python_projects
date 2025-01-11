# aprendendo sobre filter que é um filtro funcional

produtos =[
    {'nome': 'p1', 'preco': 13.20},
    {'nome': 'p2', 'preco': 55.20},
    {'nome': 'p3', 'preco': 5.20},
    {'nome': 'p4', 'preco': 22.20},
    {'nome': 'p5', 'preco': 100.67},   
]

def filtrarProduto(produto):
    return produto['preco'] > 20

produtosFiltrados = filter(filtrarProduto, produtos)
print(produtosFiltrados)
print(list(produtosFiltrados))