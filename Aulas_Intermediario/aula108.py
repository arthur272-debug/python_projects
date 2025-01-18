# Relembrando funções recursivas e recursividade

def fazerRecursao(inicio=0,fim=10):
    if inicio >= fim:
        return fim
    
    print(inicio,fim)
    
    inicio += 1
    return fazerRecursao(inicio,fim)

print(fazerRecursao())