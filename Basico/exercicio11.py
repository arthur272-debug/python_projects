# Exercício sobre Jogo da Palavra Secreta --- terminar

palavra = 'Jogo'
palavra_adivinhada = '****'
letra = ''
tentativa = 0

print('Jogo da Palavra Secreta:')

while '*' in palavra_adivinhada:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Letra Inválida!!')
        continue

    if letra in palavra:
        i = palavra.find(letra)
        palavra_adivinhada[i] = letra
    
    print(f'Palavra Secreta: {palavra_adivinhada}')
    tentativa +=1

print(f'Parabéns!!! Você adivinhou toda a palavra secreta: {palavra}')
print(f'Número de tentativas: {tentativa}')
