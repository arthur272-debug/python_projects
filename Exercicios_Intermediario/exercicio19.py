# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


# essa estrutura está 'adiando' a execução de uma outra função que foi recebida como argumento
def criar_funcao(funcao, x):
    def funcao_interna(y):
        return funcao(x, y)
    return funcao_interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(5))
print(multiplica_por_dez(10))
