# Exercícios
# 1) Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# 2) Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# 3) Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# Resolução dos exercícios
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 1)
novos_produtos = copy.deepcopy(produtos)
for novo_preco in novos_produtos:
    novo_preco['preco'] = novo_preco['preco'] * 0.10  # 10%
print('Lista dos novos produtos com o aumento de 10%:\n', novos_produtos, '\n')

# 2)
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome, key=lambda x: x['nome'], reverse=True)
print('Lista dos produtos ordenados pelo nome em ordem descrescente:\n',
      produtos_ordenados_por_nome, '\n')

# 3)
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco, key=lambda x: x['preco'])
print('Lista dos produtos ordenados pelo preço em ordem crescente:\n',
      produtos_ordenados_por_preco, '\n')
