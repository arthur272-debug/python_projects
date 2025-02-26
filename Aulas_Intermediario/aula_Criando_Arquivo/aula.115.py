# aprendendo sobre os.remove; os.unlink e os.rename 

import os

caminho_arquivo = 'D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Aulas_Intermediario\\aula_Criando_Arquivo\\'
caminho_arquivo += 'aula115_arquivo.txt'

print('Criando arquivo...')
with open(caminho_arquivo,'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção!!!\n')
    arquivo.write('Line 1\n')
    arquivo.write('Line 2\n')
    arquivo.write('Line 3\n')
    arquivo.write('Line 4\n')
    
print('Arquivo criado!')
#os.rename(caminho_arquivo,'D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Aulas_Intermediario\\aula_Criando_Arquivo\\aula11568_arquivo.txt')
#print('Arquivo renomeado!')

os.remove(caminho_arquivo)
print('Arquivo removido!')
