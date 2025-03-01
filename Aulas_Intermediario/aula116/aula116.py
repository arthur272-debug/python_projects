# Aprendendo Python em JSON com o módulo json	

import json

caminho_arquivo ='D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Aulas_Intermediario\\aula116\\'
caminho_arquivo += 'aula_116.json'

pessoa ={
    'nome':'Arthur',
    'idade': 36,
    'cursos': ['Inglês','Python'],
    'endereco':[
        {'rua':'Rua dos bobos','numero':0},
        {'rua':'Otávio Miranda','numero':100},
    ],

}

# Aprendendo a escrever em JSON
# with open(caminho_arquivo,'w', encoding='utf8') as arquivo:
#     json.dump(pessoa,arquivo, indent=4, ensure_ascii=False)

# Aprendendo a ler em JSON
with open(caminho_arquivo,'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    print(dados)

print(dados['endereco'][0]['rua'])