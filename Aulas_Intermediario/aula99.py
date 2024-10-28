# Decoradores com parâmetros

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwards):
            print('Exemplo 2')
            res = func(*args, **kwards)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x+y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x*y)
exemplo1 = soma(10, 5)
exemplo2 = multiplica(15, 4)
print(exemplo1)
print(exemplo2)
