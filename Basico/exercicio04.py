# Exercício sobre fatiamento e formatação de strings 

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
tam = len(nome)

if (idade and nome):
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if(" " in nome):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    
    print(f'Seu nome tem {tam} letras')
    print(f'A primeira letra do seu nome é {nome[1]}')
    print(f'A última letra do seu nome é {nome[tam]}')
else:
    print('Desculpe, você deixou campos vazios.')
