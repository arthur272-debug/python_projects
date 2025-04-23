# Revisando a parte de escopo - classe e métodos da classe


class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    variavel = "nome"
    print(variavel)

    def comer_alimento(self, alimento):
        self.alimento = alimento
        print(f"{self.nome} comeu {self.alimento}")

    def executar(self, *args, **kwargs):
        return self.comer_alimento(*args, **kwargs)


cachorro = Animal(nome="Rex", especie="Cachorro")
print(cachorro.nome)
print(cachorro.especie)
print(cachorro.executar("ração"))
