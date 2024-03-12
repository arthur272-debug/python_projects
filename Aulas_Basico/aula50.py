# Revisão de split, join e strip

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
lista_palavras2 = frase.split('- ')

print(lista_palavras2)
print(lista_palavras)

lista_nova = []

for i, frase in enumerate(lista_palavras):
    lista_nova.append(lista_palavras[i].strip())

frases_unidas = ', '.join(lista_palavras)
print(frases_unidas)
