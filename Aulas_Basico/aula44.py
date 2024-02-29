# Cuidados com dados mutáveis

lista_a =['Luiz','Maria',1,True,1.2]
lista_b = lista_a
lista_c= lista_a.copy()

lista_c[0] = 'Tutu'

print(lista_a)
print(lista_b)
print(lista_c)