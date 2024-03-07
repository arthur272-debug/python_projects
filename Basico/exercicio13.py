"""
--> Faça uma lista de comprar com listas
--> O usuário deve ter a possibilidade de
--> inserir, apagar e listar valores da sua lista
--> Não permita que o programa quebre com 
--> erros de índices inexistentes na lista.
terminar ainda
"""
import os
termina_lista = False
opcao = ''
lista = []

print(f'Lista de compras:\t')

while (termina_lista == False):
    opcao = input(f'Selecione uma opção \t [i]nserir [a]pagar [l]istar:')
    opcao = opcao.lower()
    if (opcao =='i'):
        item = input('Digite o item:')
        lista.append(item)
    elif (opcao == 'l'):
        itens = lista.count()
        if(itens== 0):
            print('Lista vazia: nada para listar.')    
        else:
            for indice, nome in enumerate(lista):
                print(indice,nome)
    elif (opcao == 'a'):
        item = input('Qual indice você quer deletar?')
        #if lista.index(item)