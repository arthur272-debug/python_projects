# Exercícios
# 1) Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# 2) Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# 3) Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# Resolução dos exercícios
from dados import produtos  # tem que ter o __init__.py - para ter nenhum problema
import copy

print('Lista de produtos originais:\n', produtos, '\n')
# 1)
novos_produtos = copy.deepcopy(produtos)
for novo_preco in novos_produtos:
    novo_preco['preco'] = round(novo_preco['preco'] * 1.1, 2)  # 10% -> 1.1
print('Lista dos novos produtos com o aumento de 10%:\n', novos_produtos, '\n')

# 2)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda x: x['nome'], reverse=True)
print('Lista dos produtos ordenados pelo nome em ordem descrescente:\n',
      produtos_ordenados_por_nome, '\n')

# 3)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), key=lambda x: x['preco'])
print('Lista dos produtos ordenados pelo preço em ordem crescente:\n',
      produtos_ordenados_por_preco, '\n')
