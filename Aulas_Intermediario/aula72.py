# Revisão a função lambda - ver na parte do material

def exibir(lista):
    for item in lista:
        print(item)
    print()


lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista1 = sorted(lista, key=lambda item: item['nome'])
lista2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista1)
exibir(lista2)
