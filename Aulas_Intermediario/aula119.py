# aprendendo sobre Positional_Only parameters e Keyword_Only parameters


# Positional_Only parameters
def somarNumeros(a, b, /):
    return a + b


def somarNumeros2(a, b, /, c, d):
    return a + b + c + d


def somarNumeros3(a, b, *, c, d):
    return a + b + c + d


def somarNumeros4(*, a, b):
    return a + b


print(somarNumeros(1, 2))
print(somarNumeros2(1, 2, 3, d=4))
print(somarNumeros3(1, 2, c=9, d=41))
print(somarNumeros4(a=1, b=2))