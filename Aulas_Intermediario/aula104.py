# groupby - itertools

from itertools import groupby

alunos =[
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Julia', 'nota': 'A'},
    {'nome': 'Zeca', 'nota': 'C'},
    {'nome': 'Marcos', 'nota': 'B'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Luiza', 'nota': 'D'},
]

def ordenarAluno(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordenarAluno)
grupos_notas = groupby(alunos_agrupados, key=ordenarAluno)

print('Notas dos alunos:')
for nota, grupo in grupos_notas:
    print(f'\nNota {nota}:')
    for aluno in grupo:
        print(f'\t{aluno["nome"]}')