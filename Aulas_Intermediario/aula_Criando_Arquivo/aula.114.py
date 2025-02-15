# Praticando os modos de abertura de arquivos além do encoding com with open

caminho_arquivo = 'D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Aulas_Intermediario\\aula_Criando_Arquivo\\'
caminho_arquivo += 'aula114_arquivo.txt'

with open(caminho_arquivo,'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção!!!\n')
    arquivo.write('Line 1\n')
    arquivo.write('Line 2\n')
    arquivo.writelines(
        ('Line 3\n','Line 4\n','Line 5\n')
    )