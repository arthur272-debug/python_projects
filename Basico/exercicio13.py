"""
--> Faça uma lista de comprar com listas
--> O usuário deve ter a possibilidade de
--> inserir, apagar e listar valores da sua lista
--> Não permita que o programa quebre com 
--> erros de índices inexistentes na lista.
"""
import os
termina_lista = False
opcao = ''
lista = []



while (termina_lista == False):
    print(f'Lista de compras:\t')
    opcao = input(
        f'Selecione uma opção --> [i]nserir [a]pagar [l]istar [e]ncerrar: ')
    opcao = opcao.lower()
    tamanho = len(lista)
    if (opcao == 'i'):
        os.system('cls')
        item = input('Digite o item:')
        lista.append(item)
    elif (opcao == 'l'):
        os.system('cls')
        if (tamanho == 0):
            print('Lista vazia: nada para listar.')
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)

    elif (opcao == 'a'):
        indice = input('Qual indice você quer deletar? ')
        try:
            indice = int(indice)
        except:
            print('Item inválido!! Por favor, digite outro. ')
            continue

        if (indice > tamanho) or (tamanho == 0):
            print('Índice não existe.')
        else:
            item = lista[indice]
            lista.remove(item)
            print(f'Item {item} foi removido da lista de compras.')
    elif (opcao == 'e'):
        os.system('cls')
        if (tamanho == 0):
            print('Lista vazia: nada para listar.')
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)

        termina_lista = True
    else:
        print('Opção Inválida!!')
