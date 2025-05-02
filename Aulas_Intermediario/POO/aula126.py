# aprendendo sobre __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


pessoa1 = Pessoa("Valéria", 29)
pessoa2 = Pessoa("Ígor", 34)
print(pessoa2.__dict__)
pessoa2.__dict__["outra_chave"] = "valor"
pessoa2.__dict__["nome"] = "João"
print(pessoa2.__dict__)

print(pessoa1.__dict__)
print(vars(pessoa1))

dados = {
    "nome": "Lucas",
    "idade": 25,
}

pessoa3 = Pessoa(**dados)
print(vars(pessoa3))
