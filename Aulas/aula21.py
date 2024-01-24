# Operadores in e not in

# nome = 'Tutu'
# print(nome[2])
# print(nome[-3])
# print('a' not in nome)
# print('a' in nome)
# print('u' in nome)
# print('tu' in nome)

nome = input("Digite um nome: ")
encontrar = input("Digite o que encontrar: ")

if (encontrar in nome):
    print(f'{encontrar} está em {nome}.')
else:
    print(f"{encontrar} não está em {nome}.")