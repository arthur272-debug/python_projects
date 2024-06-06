# alguns exemplos de lambda

def executa(funcao, *args):
    return funcao(*args)


# nome de função/ retorno/ argumentos - lambda
print(executa(lambda x, y: x+y, 2, 3))  # função de soma

duplica = executa(lambda m: lambda n: m*n, 2)
print(duplica(2))  # função de multiplica

# função de somatório de números
print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8))
