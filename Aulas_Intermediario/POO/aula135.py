# Revisando sobre a relação de composição -> relação entre classes


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def adicionar_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(f"Rua: {endereco.rua}, Número: {endereco.numero}")


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f"Endereco {self.rua}, {self.numero} foi removido.")


cliente1 = Cliente("Luiz")
cliente1.adicionar_endereco("Rua João Ovo", 90)
cliente2 = Cliente("Maria")
cliente2.adicionar_endereco("Rua das Flores", 560)

print(cliente1.enderecos[0].rua)
print(cliente2.enderecos[0].rua)

cliente1.listar_endereco()
cliente2.listar_endereco()

del cliente2

print("Código acabado")
