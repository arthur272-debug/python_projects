# Imprecisão do ponto flutuante

import decimal


numero_01 = 0.5
numero_02 = 0.7
numero_03 = numero_01+numero_02
numero_04 = decimal.Decimal('0.2')
numero_05 = decimal.Decimal('0.5')
numero_06 = numero_04+ numero_05
print(numero_03)
print(numero_06)
print(f'{numero_03:.2f}')
print(round(numero_03,2))