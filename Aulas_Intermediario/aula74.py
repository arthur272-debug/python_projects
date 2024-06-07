# Empacotamento e desempacotamento de dicionários


def mostrar_argumentos(*args, **kwargs):
    print('Não Nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


pessoa = {
    'nome': 'Tutu',
    'sobrenome': 'Andrade'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

configuracoes = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
}

print('Teste 1:')
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

print('\nTeste 2:')
for chave, valor in pessoa.items():
    print(f'Chave: {chave}, Valor: {valor}')


pessoas_completa = {**pessoa, **dados_pessoa}

print('\nTeste 3:')
mostrar_argumentos(**pessoas_completa)

print('\nTeste 4:')
mostrar_argumentos(**configuracoes)
