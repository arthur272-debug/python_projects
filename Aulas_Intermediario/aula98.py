# Funções decoradoras com a sintaxe @

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@criar_funcao  # fazendo automaticamente a decoradora
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('O parâmetro passado deve ser uma string.')


string_invertida = inverte_string('12345')
print(string_invertida)
