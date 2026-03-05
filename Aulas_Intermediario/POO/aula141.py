# Praticando e entendendo sobre a herança múltipla


class A:
    def imprimirIdentificacao(self):
        return "Classe A"


class B(A):
    def imprimirIdentificacao(self):
        return "Classe B"

    def imprimirOutro(self):
        return "Método da classe B"


class C(A): ...


class D(B, C):
    # def imprimirIdentificacao(self):
    #     return "Classe D"
    ...


identidade = D()
print(identidade.imprimirIdentificacao())
print(identidade.imprimirOutro())
print(D.mro())  # Mostra a ordem de resolução de métodos (Method Resolution Order)
