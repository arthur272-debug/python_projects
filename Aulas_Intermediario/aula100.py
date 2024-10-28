# Ordem dos decoradores

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def criar_funcao_nova(*args, **kwards):
            res = func(*args, **kwards)
            final = f'{res} {nome}'
            return final
        return criar_funcao_nova
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x+y


exemplo01 = soma(10, 5)
print(exemplo01)
