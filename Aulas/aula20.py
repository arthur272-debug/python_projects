# Revisão sobre o operador NOT

senha = input('Senha:')

if senha != '123456':
    print('Senha incorreta!')

if not senha:
    print('Você não digitou nada!')

print(not 0)
print(not 1)