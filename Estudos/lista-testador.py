from time import sleep

from listaDinEncOrd import ListaDinEncOrd
from listaEstEncOrd import *


def main():
    while True:
        escolha = int(input("1 - Lista Estática Encadeada\n2 - Lista Dinâmica Encadeada\nEscolha: "))

        if escolha == 1:
            tamanho = int(input("Tamanho da fila: "))
            lista = ListaEstaticaEncadeada(tamanho)
            break
        elif escolha == 2:
            lista = ListaDinEncOrd()
            break
        else:
            print("Opção inválida!")
            print()
    print()

    while True:
        opcao = int(
            input(
                "1 - Adicionar\n2 - Remover\n3 - Consultar\n4 - Atualizar\n5 - Mostrar\n6 - Esvazia\n7 - Reorganiza por CPF\n8 - Sair\nEscolha: "
            )
        )
        print()

        if opcao == 1:
            nome: str = input("Digite o nome: ")
            idade: int = int(input("Digite a idade: "))
            cpf: str = input("Digite o cpf: ")
            if lista.inserir(TipoItem(nome=nome, idade=idade, cpf=cpf)):
                print(f"{nome} adicionado com sucesso!")
            else:
                print("fila cheia!")
        elif opcao == 2:
            nome = input("Digite o nome de quem deseja remover: ")
            if lista.remover(nome):
                print(f"{nome} removido!")
            else:
                print("Lista vázia ou item não encontrado")
        elif opcao == 3:
            nome = input("Digite o nome: ")
            item = lista.consultar(nome)
            if item == None:
                print("Fila vázia ou Não encontrado")
            else:
                print(f"Nome: {item.nome}\nIdade: {item.idade}\nCPF: {item.cpf}")
        elif opcao == 4:
            nome: str = input("Digite o nome: ")
            idade: int = int(input("Digite a idade: "))
            cpf: str = input("Digite o cpf: ")

            if lista.atualizar(TipoItem(nome=nome, idade=idade, cpf=cpf)):
                print(f"{nome} atualizado!")
            else:
                print("Lista vázia ou nome não encontrado")
        elif opcao == 5:
            lista.mostrar()
        elif opcao == 6:
            opcao = int(input("Tem certeza que deseja limpar tudo?\n1 - Sim\n2 - Não\nEscolha: "))

            if opcao == 1:
                lista.esvazia()
                print("Lista esvaziada!")
            elif opcao == 2:
                print("Ação cancelada!")
        elif opcao == 7:
            lista.reordenaCpf()
            lista.mostrar()
        elif opcao == 8:
            print("Encerrando programa...")
            sleep(2)
            print("🖕")
            break
        else:
            print("Opção inválida")
        print()


if __name__ == "__main__":
    main()
