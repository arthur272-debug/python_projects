# Entendendo sobre Zip e zip-longest 
from itertools import zip_longest

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = ['oi', 'tudo', 'bem', 'com', 'você']
combinado = zip(lista1, lista2)
combinado_inverso= zip_longest(lista1, lista2)
print(f'Ordem normal: {list(combinado)}')
print(f'Ordem inversa {list(combinado_inverso)}')