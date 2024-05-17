# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
perguntas_acertadas = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print('Opções:')
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
    resposta = input('Escolha uma opção:')
    if resposta.isdigit():
        resposta = int(resposta)
        if pergunta['Opções'][resposta] == pergunta['Resposta']:
            print('Acertou!\n')
            perguntas_acertadas += 1
        else:
            print('Errou!\n')
    else:
        print('Opção Inválida!\n')

print(f'Você acertou {perguntas_acertadas} de', len(perguntas), 'perguntas.')
