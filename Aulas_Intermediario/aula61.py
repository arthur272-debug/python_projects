# Higher Order Functions  - Conceitos

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)

print(
    executa(saudacao, 'Bom dia', 'Maria')
)
