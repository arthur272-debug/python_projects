# Exercício guiado - Iterando strings com o while

nome ='Tutuão Fabroso'

tamanho_nome = len(nome)
print('Tamanho do nome:',tamanho_nome)
contador =0

while contador<tamanho_nome:
    print(nome[contador])
    contador +=1

nova_string=''
contador=0

while contador<tamanho_nome:
    letra = nome[contador]
    nova_string+=letra
    contador+=1

print(nova_string)