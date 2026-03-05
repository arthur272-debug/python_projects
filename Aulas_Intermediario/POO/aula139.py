# Aprendendo Herança Simples em Python - Sintaxe
class Pessoa:
    cpf = "123456789"

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def expressarComprimento(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Maquinista(Pessoa):
    def expressarComprimento(self):
        print(
            f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou maquinista de trem."
        )


class Motorista(Pessoa): ...


cpf = "987654321"


p1 = Maquinista("Thiago", 30, "Masculino")
p1.expressarComprimento()
p2 = Motorista("Maria", 25, "Feminino")
p2.expressarComprimento()
