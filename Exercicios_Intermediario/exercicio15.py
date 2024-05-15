# Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro

def multiplicador_numero(multiplicador):
    def multiplicar_numero(numero):
        return numero * multiplicador
    return multiplicar_numero


duplicar = multiplicador_numero(2)
print(duplicar(2))
