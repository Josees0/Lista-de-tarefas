# Lista de tarefas
tasks = []

# Adicionar tarefa
def add_task(task):
    tasks.append(task)
    print("Tarefa adicionada com sucesso")

# Listar tarefas
def list_tasks():
    if tasks:
        print("Lista de tarefas:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Não há tarefas na lista")

# Remover tarefa
def remove_task(index):
    try:
        del tasks[index - 1]
        print("Tarefa removida com sucesso")
    except IndexError:
        print("Índice inválido. Tarefa não encontrada")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Visualizar lista de tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

    choice = input("Digite o número da opção: ")

    if choice == "1":
        task = input("Digite uma nova tarefa: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        if tasks:
            index = int(input("Digite o número da tarefa que deseja remover: "))
            remove_task(index)
        else:
            print("Não há tarefas para remover.")
    elif choice == "4":
        print("Saindo da lista de tarefas...")
        break
    else:
        print("Opção inválida. Tente novamente.")
#pode usar esse código a vontade @josees0
