# Salvando a classe em um arquivo por meio do json
# Exercicio: salvar os dados de uma classe em um arquivo json e
# depois criar as instâncias da classe a partir desse arquivo json.
# Salvando a classe em um arquivo json

import json

CAMINHO_ARQUIVO = (
    "D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Exercicios_Intermediario\\POO"
)


class Carro:
    def __init__(self, modelo, ano, cor, marca):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.marca = marca


carro1 = Carro("Fusca", 1980, "azul", "Volkswagen")
carro2 = Carro("Civic", 2020, "preto", "Honda")
carro3 = Carro("Civic", 2020, "preto", "Honda")

dados = [vars(carro1), vars(carro2), vars(carro3)]


def salvar_dados():
    with open(CAMINHO_ARQUIVO + "/carros.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


if __name__ == "__main__":
    salvar_dados()
    print("Dados salvos com sucesso!")
