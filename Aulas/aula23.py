'''
Formatação de strings - (f-strings)
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
'''

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{variavel:$^10}')
print(f'{1000.484663187:.1f}')
print(f'{9000.4846656546573187:,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')