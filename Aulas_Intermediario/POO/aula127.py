# aprendendo sobre os métodos de classe - @classmethod _ factories methods


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def dizer_hello(cls):
        print("Hello")

    @classmethod  # factory method
    def criar_pessoa_com_idade(cls, nome):
        return cls(nome, 30)

    @classmethod
    def criar_pessoa_anonima(cls, idade):
        return cls("Anônimo", idade)


p1 = Pessoa("Lucas", 20)
p2 = Pessoa.criar_pessoa_com_idade("Coura")
p2.dizer_hello()
p3 = Pessoa.criar_pessoa_anonima(25)
print(p3.dizer_hello(), p3.nome, p3.idade)
