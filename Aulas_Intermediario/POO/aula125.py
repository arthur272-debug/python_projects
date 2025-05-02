# revisando os atributos de classe
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


pessoa1 = Pessoa("Lucas", 25)
pessoa2 = Pessoa("Maria", 30)

print(f"{pessoa1.nome} nasceu em {pessoa1.get_ano_nascimento()}")
print(f"{pessoa2.nome} nasceu em {pessoa2.get_ano_nascimento()}")
