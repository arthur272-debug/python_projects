# aula sobre iterador/next/iter

texto = 'canada' # iterável

iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break