"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_str = input('Digite a hora desejada: ')

try:
   hora_int = int(hora_str)

   if (hora_int >= 0) and (hora_int <= 11) or (hora_int == 24):
       print('Bom dia/ Buenos días/ Good morning!!')
   elif (hora_int >= 12) and (hora_int <= 17):
      print('Boa tarde/ Buenas tardes/ Good afternoon!!')  
   elif (hora_int >=18) and (hora_int <= 23):
      print('Boa noite/ Buenas noches/ Good evening!!')
   else:
      print('Hora inválida!! Por favor, digite uma hora válida.')
except:
   print('Número inválido!! Digite um número válido!!')