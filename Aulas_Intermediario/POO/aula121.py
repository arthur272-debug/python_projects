# Revisando sobre o método __init__

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

c1 = Carro('Fusca', 'Volkswagen')
c2 = Carro('Civic', 'Honda')

print(c1.nome, c1.marca)
print(c2.nome, c2.marca)