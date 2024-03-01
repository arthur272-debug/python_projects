# Exercício para exibir os índices da Lista

lista =['Maria','Arthur','Luiz',1,255,5]
contador = 0

for conteudo in lista:
    print(f'{contador} {conteudo}')
    contador+=1

# Outra forma de fazer o exercício

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))