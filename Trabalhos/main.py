from trabalho1 import ListaDinamicaEncadeada, TipoItem

ACOUGUE = 1
PADARIA = 2
FRIOSELATICINIOS = 3
HIGIENECORPORAL = 4
LIMPEZA = 5
HORTIFRUTI = 6
GRAOSFARINACEOSECAFE = 7
BEBIDAS = 8
UTENSILIOS = 9
DIVERSOS = 10

def inserirDadosTeste(lista: ListaDinamicaEncadeada) -> None:
    produtos = [
        TipoItem("Arroz", 7, 50, 20, 20.00, 28.00),
        TipoItem("Acucar", 7, 3, 15, 3.50, 5.00),
        TipoItem("Alcatra", 1, 0, 30, 35.00, 45.00),
        TipoItem("Banana", 6, 25, 40, 3.00, 5.00),
        TipoItem("Cafe", 7, 12, 18, 12.00, 17.00),
        TipoItem("Cerveja", 8, 100, 60, 3.00, 5.00),
        TipoItem("Detergente", 5, 4, 25, 1.50, 2.50),
        TipoItem("Feijao", 7, 35, 22, 6.00, 9.00),
        TipoItem("Farinha", 7, 0, 12, 4.00, 6.50),
        TipoItem("Frango", 1, 18, 27, 10.00, 15.00),
        TipoItem("Iogurte", 3, 2, 14, 2.50, 4.00),
        TipoItem("Leite", 3, 40, 50, 4.00, 6.00),
        TipoItem("Macarrao", 7, 60, 10, 3.00, 5.00),
        TipoItem("Maca", 6, 5, 16, 4.00, 7.00),
        TipoItem("Pao", 2, 0, 80, 0.50, 1.00),
        TipoItem("Papel Higienico", 4, 8, 20, 8.00, 12.00),
        TipoItem("Queijo", 3, 15, 13, 25.00, 35.00),
        TipoItem("Sabonete", 4, 3, 17, 1.80, 3.00),
        TipoItem("Refrigerante", 8, 30, 45, 5.00, 8.00),
        TipoItem("Vassoura", 9, 7, 5, 8.00, 14.00),
    ]

    for produto in produtos:
        lista.insere(produto)

    print(f"{len(produtos)} produtos de teste inseridos!")


def main():
    lista = ListaDinamicaEncadeada()

    inserirDadosTeste(lista)

    print("\nProdutos cadastrados:")
    lista.mostra()

    lista.relatorioEstoqueTotal()
    lista.relatorioEstoqueTipo(ACOUGUE)
    lista.relatorioProdutosEsgotados()
    lista.relatorioProdutosEstoqueBaixo(10)
    lista.relatorioQuantidadeVendida()
    print()

if __name__ == "__main__":
    main()
