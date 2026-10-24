from filaDinamica import FilaDinamica
from filaEstaticaCircular import FilaEstaticaCircular, TipoItem


def main():
    while True:
        escolha = int(input("1 - Fila Estática Circular\n2 - Fila Dinâmica\nEscolha: "))

        if escolha == 1:
            tamanho = int(input("Tamanho da fila: "))
            fila = FilaEstaticaCircular(tamanho)
            break
        elif escolha == 2:
            fila = FilaDinamica()
            break
        else:
            print("Opção inválida!")
            print()
    print()

    while True:
        opcao = int(
            input(
                "1 - Adicionar\n2 - Remover\n3 - Primeiro\n4 - Mostrar\n5 - Esvazia\n6 - Sair\nEscolha: "
            )
        )
        print()

        if opcao == 1:
            item = input("Digite o valor: ")
            if fila.enfileira(TipoItem(item)):
                print(f"{item} adicionado com sucesso!")
            else:
                print("fila cheia!")
        elif opcao == 2:
            item = fila.primeiro()
            if fila.desenfileira():
                print(f"{item.valor} removido!")
            else:
                print("fila vázia!")
        elif opcao == 3:
            item = fila.primeiro()
            if item == None:
                print("Fila vázia!")
            else:
                print(f"O primeiro da fila é {item.valor}")
        elif opcao == 4:
            fila.mostra()
        elif opcao == 5:
            opcao = int(input("Tem certeza que deseja limpar tudo?\n1 - Sim\n2 - Não\nEscolha: "))

            if opcao == 1:
                fila.esvazia()
                print("fila esvaziada!")
            elif opcao == 2:
                print("Ação cancelada!")
    
        elif opcao == 6:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")
        print()


if __name__ == "__main__":
    main()
