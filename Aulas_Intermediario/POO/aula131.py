# aprendendo sobre @property + @setter -> getter e setter


class Caneta:
    def __init__(self, cor, cor_tampa):
        self._cor = cor
        self._cor_tampa = cor_tampa

    @property
    def cor(self):
        return self._cor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta("azul", "preto")
print(caneta.cor_tampa)  # usando o getter
print(caneta.cor)
caneta.cor = "vermelho"  # usando o setter
print(caneta.cor)
