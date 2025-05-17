# aprendendo sobre o @staticmethod - geralmente usado para criar métodos que não precisam de acesso a instância ou classe


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @staticmethod
    def criar_pessoa(nome):
        return Pessoa(nome)


pessoa1 = Pessoa.criar_pessoa("Lucas")
pessoa2 = Pessoa.criar_pessoa("João")
print(pessoa1.nome)
print(pessoa2.nome)
