# Fitro de dados em list comprehension

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(f'Números pares:{numeros_pares}')

numeros = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 12, 14]
numeros_pares2 = list(filter(lambda num: num % 2 == 0, numeros))
print(f'Números pares 2:{numeros_pares2}')
