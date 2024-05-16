# Revisando métodos úteis do dict

doc1 = {
    'nome': 'TutuRio',
    'sobrenome': 'Free Fire'
}
# pop
nome = doc1.pop('nome')
print(nome)

# popitem
ultima_chave = doc1.popitem()
print(ultima_chave)

# update

doc1.update({
    'nome': 'Outro Nome',
    'sobrenome': 'Qualquer coisa'
})
print(doc1)

# outra maneira de fazer a atualização
doc1.update(nome='Pica-Pau', sobrenome='vermelho')
print(doc1)
