# Valores padrão para funções Python + NoneType e None

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x+y+z)
    else:
        print(f'{x=} {y=}', x+y)


soma(2, 5, 8)
soma(26, 50)
soma(80, 50)
soma(90, 80, 100)
