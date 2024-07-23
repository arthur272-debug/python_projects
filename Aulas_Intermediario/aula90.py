# Revisando raise - exceções

def verificarDivisor(numero):
    if numero == 0:
        raise ZeroDivisionError('Não é possível dividir número por 0!!')
    else:
        return True


def dividirNumeros(numero, numero2):
    verificarDivisor(numero2)

    return numero/numero2


# print(dividirNumeros(8, 2))

try:
    resultado = dividirNumeros(9, 0)
except ValueError as e:
    print(f'Erro: {e}')
