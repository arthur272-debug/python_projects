# Revisão de List comprehension em Python

lista = []
for numero in range(10):
    lista.append(numero)

# list comprehension
lista2 = [
    numero * 2
    for numero in range(10)
]
print(lista)
print(lista2)
