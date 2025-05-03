# Recuperando o arquivo com os dados da classe e criando as suas instâncias

import json
from exercicio24_a import CAMINHO_ARQUIVO, Carro

with open(CAMINHO_ARQUIVO + "/carros.json", "r") as arquivo:
    dados = json.load(arquivo)
    carro1 = Carro(**dados[0])
    carro2 = Carro(**dados[1])
    carro3 = Carro(**dados[2])

print(carro1.__dict__)
print(carro2.__dict__)
print(carro3.__dict__)
