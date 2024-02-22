# revisão sobre for in

frase = 'cebolaa'
novo_texto = ''

for letra in frase:
    print(letra)
    novo_texto += f'*{letra}'

print(novo_texto)