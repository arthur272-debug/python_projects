# try, except, else e finally

try:
    a = 1000
    b = 2
    # b = 0
    c = 12
    # adh
    # a = a[3]-0
    d = a/b

except (ZeroDivisionError, NameError, TypeError) as error:
    print('Erro:', error)
    print('Tipo de erro:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO!!')

else:  # será excutado quando o código não for levantado a exceção
    print('Código executado sem nenhum erro!')

finally:  # Sempre será executado
    print('Código encerrado!!')
