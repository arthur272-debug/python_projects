# aula sobre dir, hasattr e getattr

string = 'Arthur'
metodo = 'lower'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
