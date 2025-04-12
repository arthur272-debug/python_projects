# Salvando a lista de tarefas em um arquivo JSON e usando o arquivo como base de dados

import json

def adicionar_tarefa(tarefas, tarefa):
    if not tarefa.strip():
        print("Tarefa inválida.")
        return
        
    tarefas.append(tarefa)
    print("Tarefa adicionada na lista!")


def listar_tarefas(tarefas):
    if len(tarefas) == 0:
            print("Não há tarefas para listar.")
    else:
        print("Tarefas:")
        for tarefa in tarefas:
            print(f"- {tarefa}")
    
    return

def refazer_tarefa(tarefas, tarefas_desfeitas):
    if len(tarefas_desfeitas) == 0:
        print("Não há tarefas para refazer.")
    else:
        tarefas.append(tarefas_desfeitas.pop())
    
    return

def desfazer_tarefa(tarefas, tarefas_desfeitas):
    if len(tarefas) == 0:
        print("Não há tarefas para desfazer.")
    else:
        tarefas_desfeitas.append(tarefas.pop())
    
    return

def salvar_dados(tarefas, caminho_arquivo):
    dados = tarefas
    try:
        with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
           dados = json.dump(tarefas, arquivo,indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")
    
    return dados


def ler_arquivo(tarefas,caminho_arquivo):
    dados =[]
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            return tarefas
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        salvar_dados(tarefas, caminho_arquivo)    
        
    return dados


CAMINHO_ARQUIVO = 'D:\\Docs_Arthur\\Projetos_cursos\\python_projects\\Exercicios_Intermediario\\exercicio23'
CAMINHO_ARQUIVO += '\\tarefas.json'
comando = None
tarefas = ler_arquivo([], CAMINHO_ARQUIVO)
tarefas_desfeitas = []

while True:
    print("\nLista de tarefas:\n")
    print("- listar;")
    print("- adicionar;")
    print("- desfazer;")
    print("- refazer; e")
    print("- sair.\n")
    
    tarefa = input("-> Digite uma opção: ")
    
    comandos_validos ={
        'listar': lambda: listar_tarefas(tarefas),
        'adicionar': lambda: adicionar_tarefa(tarefas, input("Digite a tarefa a ser adicionada: ")),
        'desfazer': lambda: desfazer_tarefa(tarefas, tarefas_desfeitas),
        'refazer': lambda: refazer_tarefa(tarefas, tarefas_desfeitas),
        'sair': lambda: exit()
    }
    comando =comandos_validos.get(tarefa) if comandos_validos.get(tarefa) else \
        lambda: print("Comando inválido.")
    
    comando()
    salvar_dados(tarefas, CAMINHO_ARQUIVO)
