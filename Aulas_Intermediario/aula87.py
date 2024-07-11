# Try, except, else e finally - Review (parte 1)

try:
    a = 2
    b = 0
    c = 12
    # f
    # a = a[3]-0
    d = a/b
except ZeroDivisionError:
    print('Erro por divisão!')
except NameError:
    print('Variável não definida!')
except Exception:
    print('Erro Desconhecido!')

print('Código encerrado!!')
