# Praticando a sintaxe 'super' e a sobreposição de métodos


class MinhaString(str):
    def upper(self):
        resultado = super().upper()
        print("Usando o método upper da classe pai")
        return f"String em maiúsculas: {resultado}"

    def lower(self):
        resultado = super().lower()
        print("Usando o método lower da classe pai")
        return f"String em minúsculas: {resultado}"


word = MinhaString("Python é Incrível!")
print(word.upper())
print(
    MinhaString.mro()
)  # Mostra a ordem de resolução de métodos (Method Resolution Order)
