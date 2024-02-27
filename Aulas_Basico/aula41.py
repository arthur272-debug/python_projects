# revisão sobre sobre os métodos principais do Tipo List

lista =[10,20,30,40]
numero = lista[2]
lista[2] = 300
print(lista)
del(lista[2])
print(numero)
print(lista)
lista.append(50)
print(lista)
removido = lista.pop()
print("O item que foi removido é",removido)
print(lista)