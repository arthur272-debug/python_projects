'''  
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = "Arthur"
preco = 1000.95897643
variavel = '%s, o preço é R$%.2d' % (nome,preco)
print(variavel) 
print('O hexadecimal de %d é %x' % (15,15))
print('O hexadecimal de %d é %08x' % (15,15))