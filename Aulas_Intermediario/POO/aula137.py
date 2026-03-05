# Praticando a parte de guard clauses -> aplicando na situação dos if's

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
    print("Lista de tarefas - Digite uma opção:\n")
    print("- listar;")
    print("- adicionar;")
    print("- desfazer;")
    print("- refazer; e")
    print("- sair.\n")
    
    tarefa = input("Digite o número da opção desejada: ")
    
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
