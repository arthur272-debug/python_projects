# Variáveis livres + nonlocal(global - local)

def concatenar(string_inicio):
    valor_final = string_inicio

    def interno(valor_concatenar):
        nonlocal valor_final
        valor_final += valor_concatenar
        return valor_final
    return interno


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
print(c('e'))
print(c('f'))
