# Revisando sobre as relações entre classes -> Associação


class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f"Usando a ferramenta {self.nome} para escrever."


escritor = Escritor("Victor")
caneta = FerramentaDeEscrever("Caneta preta")
escritor.ferramenta = caneta  # Associação feita entre as classes

print(escritor.ferramenta.escrever())
print(caneta.escrever())
