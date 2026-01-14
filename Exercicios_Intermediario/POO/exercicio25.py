# Exercício com classes
# 1- Crie uma classe Carro (Nome)
# 2- Crie uma classe Motor (Nome)
# 3- Crie uma classe Fabricante (Nome)
# 4- Faça a ligação entre Carro e Motor
# OBS.: Um motor pode ser de vários carros
# 5- Faça a ligação entre Carro e Fabricante
# OBS.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

carro01 = Carro("Elétrico new")
motor1 = Motor("1.0")
fabricante1 = Fabricante("BYD")

carro01.motor = motor1
carro01.fabricante = fabricante1

carro02 = Carro("Cross")
fabricante02 = Fabricante('Volkswagen')
carro02.fabricante = fabricante02
carro02.motor = motor1

print(carro01.nome, carro01.motor.nome, carro01.fabricante.nome)
print(carro02.nome, carro02.motor.nome, carro02.fabricante.nome)