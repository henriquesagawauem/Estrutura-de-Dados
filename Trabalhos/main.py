from trabalho1 import ListaDinamicaEncadeada, TipoItem


def inserirDadosTeste(lista: ListaDinamicaEncadeada) -> None:
    produtos = [
        TipoItem("Arroz", "Grãos", 50, 20, 20.00, 28.00),
        TipoItem("Acucar", "Grãos", 3, 15, 3.50, 5.00),
        TipoItem("Alcatra", "Açougue", 0, 30, 35.00, 45.00),
        TipoItem("Banana", "Hortifruti", 25, 40, 3.00, 5.00),
        TipoItem("Cafe", "Grãos", 12, 18, 12.00, 17.00),
        TipoItem("Cerveja", "Bebidas", 100, 60, 3.00, 5.00),
        TipoItem("Detergente", "Limpeza", 4, 25, 1.50, 2.50),
        TipoItem("Feijao", "Grãos", 35, 22, 6.00, 9.00),
        TipoItem("Farinha", "Grãos", 0, 12, 4.00, 6.50),
        TipoItem("Frango", "Açougue", 18, 27, 10.00, 15.00),
        TipoItem("Iogurte", "Frios e Laticinios", 2, 14, 2.50, 4.00),
        TipoItem("Leite", "Frios e Laticinios", 40, 50, 4.00, 6.00),
        TipoItem("Macarrao", "Grãos", 60, 10, 3.00, 5.00),
        TipoItem("Maca", "Hortifruti", 5, 16, 4.00, 7.00),
        TipoItem("Pao", "Padaria", 0, 80, 0.50, 1.00),
        TipoItem("Papel Higienico", "Higiene Corporal", 8, 20, 8.00, 12.00),
        TipoItem("Queijo", "Frios e Laticinios", 15, 13, 25.00, 35.00),
        TipoItem("Sabonete", "Higiene Corporal", 3, 17, 1.80, 3.00),
        TipoItem("Refrigerante", "Bebidas", 30, 45, 5.00, 8.00),
        TipoItem("Vassoura", "Utensilios", 7, 5, 8.00, 14.00)
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


if __name__ == "__main__":
    main()