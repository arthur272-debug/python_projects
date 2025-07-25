# Aprendendo sobre o encapsulamento - modificadores de acesso (public, protected e private)


class Poo:
    def __init__(self):
        self.public = "Isto é público"
        self._protected = "Isto é protegido"

    def metodo_publico(self):
        self._metodo_protected()  # Chama o método protegido -- permitido
        print(self._protected)  # Acessa o atributo protegido -- permitido
        print(
            self.__metodo_private()
        )  # Acessa o método privado -- não permitido, mas possível dentro da classe
        return "Método público"

    def _metodo_protected(self):
        print("Acesso ao método protegido")
        return "Método protegido"

    def __metodo_private(self):
        print("Acesso ao método privado")
        return "Método privado"


exemplo = Poo()
print(exemplo.public)  # Atributo público pode ser acessado diretamente
print(exemplo.metodo_publico())  # Método público pode ser chamado diretamente
