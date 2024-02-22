# revisão sobre while/else

string = 'Bob Esponja'

iterador = 0

while iterador < len(string):
    letra = string[iterador]

    # if letra == ' ':
    #     break

    print(letra)

    iterador += 1
else:
    print('Fora da estrutura while')
