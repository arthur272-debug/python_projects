frase = 'O Python é uma linguagem de programação'

iterador = 0
letra_mais_vezes = ''
quantidade_letra_mais_vezes =0

while iterador<len(frase):
    letra_atual = frase[iterador]

    quantidade_letra = frase.count(letra_atual)

    if (quantidade_letra > quantidade_letra_mais_vezes):
        quantidade_letra_mais_vezes = quantidade_letra
        letra_mais_vezes = letra_atual

    iterador+=1

    print(f'A letra que aparaceu {quantidade_letra_mais_vezes} e a letra {letra_mais_vezes}')