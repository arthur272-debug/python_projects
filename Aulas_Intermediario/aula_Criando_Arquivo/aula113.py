# aprendendo os métodos úteis do TextIOWrapper e with open

caminho_arquivo = 'D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Aulas_Intermediario\\aula_Criando_Arquivo\\'
caminho_arquivo += 'aula113_arquivo.txt'

# Para criar um arquivo e depois escrever nele algo
with open(caminho_arquivo,'w+') as arquivo:
    print('Arquivo criado com sucesso!')
    arquivo.write('Hello, Mundinho do Tuturito!\n')
    arquivo.write('How are you today?\n')
    arquivo.writelines(('God bless you!\n','I am fine, thank you!'))
    arquivo.seek(0,0) # Função que move o cursor para o início do arquivo
    print(arquivo.read())
    print('estou Lendo o arquivo')
    arquivo.seek(0,0)
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())

print('Arquivo fechado com sucesso!')
print('*'*20)

with open(caminho_arquivo,'r') as arquivo:
    print(arquivo.read())