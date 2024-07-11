# Try, except, else e finally - Review (parte 2)

try:

    a = 2
    b = 0
    c = 12
    # f
    # a = a[3]-0
    d = a/b

except (ZeroDivisionError, NameError, TypeError) as error:  # especificando as exceções
    print('Erro:', error)  # mensagem de erro
    print('Tipo de erro:', error.__class__.__name__)  # nome do erro
except Exception:  # erros não espeficicados
    print('ERRO DESCONHECIDO!!')

print('Código encerrado!!')
