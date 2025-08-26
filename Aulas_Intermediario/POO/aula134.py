# Revisando sobre as relações entre classes -> Agregação


class Carrinho:
    def __init__(self):
        self._produtos = []

    def total_produtos(self):
        return sum([produto.preco for produto in self._produtos])

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        return self._produtos

    def adicionar_produto(self, *produtos):
        self._produtos.extend(produtos)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1 = Produto("Casaco", 10.0)
p2 = Produto("Camisa", 20.0)

carrinho.adicionar_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total_produtos())
