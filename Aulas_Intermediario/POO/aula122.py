# Revisando métodos em instâncias de classes


class Carro:
    def __init__(self, nome, cor, ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano

    def acelerar_carro(self):
        print(f"{self.nome} está acelerando!")

    def informar_carro(self):
        print(f"Nome: {self.nome}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")


fusca = Carro("Fusca", "azul", 2000)
fusca.informar_carro()
fusca.acelerar_carro()

print("\n---\n")
prius = Carro("Prius", "branco", 2010)
prius.acelerar_carro()
prius.informar_carro()
