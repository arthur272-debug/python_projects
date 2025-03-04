# Exercício - Lista de tarefas com desfazer e refazer
# Crie um programa que gerencie uma lista de tarefas. O programa deve:
# - O usuário deve poder escolher entre adicionar uma nova tarefa, listar as tarefas, 
# desfazer a última tarefa (desfazer), refazer a última tarefa (refazer). 
# O comando sair do programa é algo extra.

# revisar código

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

comando = None
tarefas = []
tarefas_desfeitas = []

while True:
    print("Lista de tarefas - Escolha uma opção:\n")
    print("1 - Adicionar tarefa;")
    print("2 - Listar tarefas;")
    print("3 - Desfazer;")
    print("4 - Refazer; e")
    print("5 - Sair do programa.\n")
    
    comando = input("Digite o número da opção desejada: ")
    
    if comando == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        listar_tarefas(tarefas)
        
    elif comando == "2":
            listar_tarefas(tarefas)
            
    elif comando == "3":
            desfazer_tarefa(tarefas, tarefas_desfeitas)
            listar_tarefas(tarefas)
            
    elif comando == "4":
            refazer_tarefa(tarefas, tarefas_desfeitas)
            listar_tarefas(tarefas)
            
    elif comando == "5":
        break
    
    else:
        print("Comando inválido.")
        
    print("\n")