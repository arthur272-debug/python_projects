# aprendendo sobre @property - tipo um getter no python


class Produto:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor


produto1 = Produto("azul")
print(produto1.cor)  # Acessando o método como se fosse um atributo
