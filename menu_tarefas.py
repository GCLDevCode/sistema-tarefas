tarefas = []

while True:
    print("\n=== MENU DE TAREFAS ===")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título da tarefa: ").strip()
        prioridade = input("Prioridade (baixa, média ou alta): ").strip().lower()

        if titulo == "":
            print("Erro: o título não pode estar vazio.")
        elif prioridade not in ["baixa", "média", "media", "alta"]:
            print("Erro: prioridade inválida.")
        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n=== LISTA DE TAREFAS ===")

            for i, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{i} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            numero = input("Número da tarefa a concluir: ")

            if not numero.isdigit():
                print("Número inválido.")
            else:
                indice = int(numero) - 1

                if 0 <= indice < len(tarefas):
                    tarefas[indice]["situacao"] = "concluída"
                    print("Tarefa atualizada com sucesso!")
                else:
                    print("Tarefa inexistente.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")