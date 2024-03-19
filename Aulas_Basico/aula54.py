# Revisão de operação ternária (condicional de uma linha)
# <valor> if <condição> else <outro valor>

# Maneira 1:

# condicao = 10 ==11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

# Maneira 2:

# digito = 9
# novo_digito = digito if digito <= 9 else 0
# print(novo_digito)

# Maneira 3:

print('Valor' if True else 'Outro valor ' if True else 'Fim')
print('Valor' if False else 'Outro valor ' if True else 'Fim')
print('Valor' if False else 'Outro valor ' if False else 'Fim')
