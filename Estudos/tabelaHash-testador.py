from time import sleep

from tabelhaHash import TabelaHash, TipoItem


def main():
    tamanho = int(input("Tamanho da tabela: "))
    tabela = TabelaHash(tamanho)
    print()

    while True:
        opcao = int(
            input(
                "1 - Adicionar\n2 - Remover\n3 - Consultar\n4 - Atualizar\n5 - Mostrar\n6 - Esvazia\n7 - Total de itens\n8 - Sair\nEscolha: "
            )
        )
        print()

        if opcao == 1:
            nome: str = input("Digite o nome: ")
            idade: int = int(input("Digite a idade: "))
            cpf: str = input("Digite o cpf: ")
            if tabela.insere(TipoItem(nome=nome, idade=idade, cpf=cpf)):
                print(f"{nome} adicionado com sucesso!")
            else:
                print("CPF já cadastrado!")
        elif opcao == 2:
            cpf = input("Digite o cpf de quem deseja remover: ")
            if tabela.remove(cpf):
                print(f"{cpf} removido!")
            else:
                print("Tabela vázia ou item não encontrado")
        elif opcao == 3:
            cpf = input("Digite o cpf: ")
            item = tabela.consulta(cpf)
            if item == None:
                print("Tabela vázia ou não encontrado")
            else:
                print(f"Nome: {item.nome}\nIdade: {item.idade}\nCPF: {item.cpf}")
        elif opcao == 4:
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            cpf = input("Digite o cpf: ")

            if tabela.atualiza(TipoItem(nome=nome, idade=idade, cpf=cpf)):
                print(f"{nome} atualizado!")
            else:
                print("Tabela vázia ou cpf não encontrado")
        elif opcao == 5:
            tabela.mostra()
        elif opcao == 6:
            opcao = int(input("Tem certeza que deseja limpar tudo?\n1 - Sim\n2 - Não\nEscolha: "))

            if opcao == 1:
                tabela.esvazia()
                print("Tabela esvaziada!")
            elif opcao == 2:
                print("Ação cancelada!")
        elif opcao == 7:
            print(f"Total de itens: {tabela.totalItens()}")
        elif opcao == 8:
            print("Encerrando programa...")
            sleep(2)
            break
        else:
            print("Opção inválida")
        print()


if __name__ == "__main__":
    main()