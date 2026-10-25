from pilhaComFila import PilhaComFila
from pilhaDinamica import PilhaDinamica
from pilhaEstatica import *


def main():
    while True:
        escolha = int(input("1 - Pilha Estática\n2 - Pilha Dinâmica\n3 - Pilha com Fila\nEscolha: "))

        if escolha == 1:
            tamanho = int(input("Tamanho da pilha: "))
            pilha = PilhaEstatica(tamanho)
            break
        elif escolha == 2:
            pilha = PilhaDinamica()
            break
        elif escolha == 3:
            pilha = PilhaComFila()
            break
        else:
            print("Opção inválida!")
            print()
    print()

    while True:
        opcao = int(input("1 - Adicionar\n2 - Remover\n3 - Topo\n4 - Mostrar\n5 - Esvazia\n6 - Sair\nEscolha: "))
        print()

        if opcao == 1:
            item = input("Digite o valor: ")
            if pilha.empilha(TipoItem(item)):
                print(f"{item} adicionado com sucesso!")
            else:
                print("Pilha cheia!")
        elif opcao == 2:
            item = pilha.topo()
            if pilha.desempilha():
                print(f"{item.valor} removido!")
            else:
                print("Pilha vázia!")
        elif opcao == 3:
            print(f"O topo da pilha é {pilha.topo().valor}")
        elif opcao == 4:
            pilha.mostra()
        elif opcao == 5:
            pilha.esvazia()
            print("Pilha esvaziada!")
        elif opcao == 6:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")
        print()
                


if __name__ == "__main__":
    main()