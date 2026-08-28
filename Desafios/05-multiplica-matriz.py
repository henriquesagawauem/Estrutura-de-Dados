import random

def geraMatriz(linhas: int, colunas: int) -> list[list[int]]:
    matriz = []
    for i in range(linhas):
        listaAux = []
        for j in range(colunas):
            listaAux.append(random.randint(1, 5))
        matriz.append(listaAux)

    return matriz

def mostraMatriz(matriz: list[list[int]]) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]} ", end="")
        print()

if __name__ == "__main__":

    eh_loop: bool = True

    matrizA: list[list[int]] = []
    matrizB: list[list[int]] = []
    

    while eh_loop:

        
        opcao = int(input("Digite sua opção\n1) Gerar Matrizes\n2) Mostrar Matrizes\n3) Multiplicar Matrizes\nOpção: "))

        if opcao == 1:
            linhasA = int(input("Digite o número de linhas da matriz A: "))
            colunasA = int(input("Digite o número de colunas na matriz A: "))

            matrizA = geraMatriz(linhasA, colunasA)
            print("Matriz gerada!")

            linhasB = int(input("Digite o número de linhas da matriz B: "))
            colunasB = int(input("Digite o número de colunas na matriz B: "))

            matrizB = geraMatriz(linhasB, colunasB)
            print("Matriz gerada!")           
        elif opcao == 2:
            print("Matriz A: \n")
            mostraMatriz(matrizA)

            print()

            print("Matriz B: ")
            mostraMatriz(matrizB)