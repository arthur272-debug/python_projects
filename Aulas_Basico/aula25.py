#Revisão de try/except

numero_str = input('Vou dobrar o número que você digitar: ')

# como deve ser(para esse caso):
# if numero_str.isdigit():
#   numero_float = float(numero_str)
#   print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
# else:
#   print('Isso não é um número!')

# como poderia ser:
try:
  print('STR:', numero_str)
  numero_float = float(numero_str)
  print('Float:',numero_float)
  print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
except:
    print('Isso não é um número!')
