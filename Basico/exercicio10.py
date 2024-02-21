frase = 'aaaaaaabbb'

iterador = 0
letra_mais_vezes = ''
quantidade_letra_mais_vezes =0
frase_lower = frase.lower()

while iterador<len(frase_lower):
    letra_atual = frase_lower[iterador]

    iterador+=1
    if letra_atual == ' ':
        continue

    quantidade_letra = frase.count(letra_atual)

    if (quantidade_letra > quantidade_letra_mais_vezes):
        quantidade_letra_mais_vezes = quantidade_letra
        letra_mais_vezes = letra_atual

print(f'A letra que aparaceu {quantidade_letra_mais_vezes}x é a letra {letra_mais_vezes}')