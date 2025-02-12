# aprendendo sobre criação de arquivos + context manager with

caminho_arquivo ='D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Aulas_Intermediario\\aula_Criando_Arquivo\\'
caminho_arquivo += 'aula112_arquivo.txt'

# Uma das formas de criar um arquivo
# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# Outra forma de criar um arquivo - padrão 
with open(caminho_arquivo, 'w') as arquivo:
    print('Arquivo criado com sucesso!')
    print('Hello, World!')
    print('Arquivo vai ser fechado')