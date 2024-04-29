# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


speak_good_morning = criar_saudacao('Good Morning')
speak_good_evening = criar_saudacao('Good Evening')

for nome in ['Maria', 'João', 'Felipe']:
    print(speak_good_morning(nome))
    print(speak_good_evening(nome))
    print(speak_good_morning(nome))
