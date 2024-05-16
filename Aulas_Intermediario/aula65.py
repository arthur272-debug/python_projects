# Estudando Shallow Copy x Deep Copy

import copy

doc1 = {
    'nome': 'Feijoada',
    'numero': 1,
    'lista1': [1, 2, 3, 4]
}

# copiando através da referência
print('Cópia por meio de referência')
doc2 = doc1

doc2['nome'] = 'Tutu'
doc2['lista1'][1] = 99999999
print(doc2)
print(doc1)

# copiando através do Shallow copy
print('Cópia por meio de Shallow copy')
doc2 = doc1.copy()
doc2['nome'] = 'Sabonete'
doc2['lista1'][1] = 9555
print(doc2)
print(doc1)

# copiando por meio do Deep copy
print('Cópia por meio de Deep copy')
doc2 = copy.deepcopy(doc1)
doc2['nome'] = 'Tutuzão'
doc2['lista1'][1] = 5555
print(doc2)
print(doc1)
