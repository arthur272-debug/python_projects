# Manipulando as chaves


pessoa = {}

chave = 'nome'

pessoa[chave] = 'Tutu'
pessoa['Sobrenome'] = 'Andrada'
print(pessoa['Sobrenome'])
print(pessoa)
pessoa[chave] = 'Livre'
del pessoa['Sobrenome']
print(pessoa)
