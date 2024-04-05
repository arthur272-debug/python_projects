# Argumentos nomeados e argumentos posicionais em funções

def soma(x, y, z):
    # Definição de função
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x+y+z)


soma(1, 2, 3)
soma(1, y=4, z=9)
soma(z=9, x=50, y=3)

print(1, 2, 3, sep='-')
