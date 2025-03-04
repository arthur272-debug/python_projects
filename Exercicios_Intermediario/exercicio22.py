# Exercício - Lista de tarefas com desfazer e refazer
# Crie um programa que gerencie uma lista de tarefas. O programa deve:
# - O usuário deve poder escolher entre adicionar uma nova tarefa, listar as tarefas, 
# desfazer a última tarefa (desfazer), refazer a última tarefa (refazer). 
# O comando sair do programa é algo extra.

comando = None
tarefas = []
tarefas_desfeitas = []

def listar_tarefas():
    if len(tarefas) == 0:
            print("Não há tarefas para listar.")
    else:
        print("Tarefas:")
        for tarefa in tarefas:
            print(f"- {tarefa}")

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
        listar_tarefas()
        
    elif comando == "2":
            listar_tarefas()
            
    elif comando == "3":
            tarefas_desfeitas.append(tarefas.pop())
            listar_tarefas()
            
    elif comando == "4":
        if len(tarefas_desfeitas) == 0:
            print("Não há tarefas para refazer.")
        else:
            tarefas.append(tarefas_desfeitas.pop())
            listar_tarefas()
            
    elif comando == "5":
        break
    
    else:
        print("Comando inválido.")
        
    print("\n")