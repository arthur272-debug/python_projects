# Exercício guiado - Calculadora com While

total =''
while True:

    num1 = input('Digite um número: ')
    num2 = input('Digite um outro número: ')
    try:
        num1 = float(num1)
        num2 = float(num2)
        operacao = input(
            'Digite a operação desejada(Adição/Subtração/Multiplicação/Divisão): ')
        operacao = operacao.lower()
        if (operacao == 'adição'):
            total = num1+num2
        elif (operacao == 'subtração'):
            total = num1-num2
        elif (operacao == 'multiplicação'):
            total = num1*num2
        elif (operacao == 'divisão'):
            total = num1/num2
        else:
            print('Operação Inválida!!')
    except:
        print('Número(s) Inválido!!')
        continue     

    print('Resultado da operação:', total)

    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')

    if sair is True:
        break
