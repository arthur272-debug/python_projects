# Exercício sobre Jogo da Palavra Secreta

palavra = 'Jogo'
letras_acertadas = ''
letra = ''
palavra_formada = ''
tentativa = 0

print('--------------Jogo da Palavra Secreta--------------')
print('')

while True:
    letra = input('Digite uma letra: ')
    palavra_formada = ''
    if len(letra) > 1:
        print('Letra Inválida!!')
        continue

    if letra in palavra:
        letras_acertadas += letra

    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            print('*')

    if palavra_formada == palavra:
        break

    tentativa += 1


print(f'Parabéns!!! Você adivinhou toda a palavra secreta: {palavra}')
print(f'Número de tentativas: {tentativa}')
