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

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print('Opções:')
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
    resposta = input('Escolha uma opção:')
    try:
        int(resposta)
    except:
        print('Reposta Inválida!!')
        continue
    if pergunta['Opções'][resposta] == pergunta['Resposta']:
        print('Acertou!')
    else:
        print('Errou!')
