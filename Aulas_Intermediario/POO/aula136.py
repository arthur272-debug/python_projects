# Aprendendo sobre o problema dos parâmetros mutáveis em funções

def adicionarCliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adicionarCliente('Arthur')
adicionarCliente('Josés',cliente1)
adicionarCliente('José',cliente1)
adicionarCliente('Tutu',cliente1)

cliente2 = adicionarCliente('Maria')
adicionarCliente('Joana',cliente2)
adicionarCliente('João',cliente2)
print(cliente1)
print(cliente2)
