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
        
def multiplicaMatriz(matrizA: list[list[int]], matrizB: list[list[int]]) -> list[list[int]]:
    
    if len(matrizA[0]) != len(matrizB):
        return []
    
    linhas = len(matrizA)
    colunas = len(matrizB[0])
    
    matrizC = []
    
    for i in range(linhas):
        listaAux = []
        
        for j in range(colunas):
            soma = 0
            
            for k in range(len(matrizB)):
                soma += matrizA[i][k] * matrizB[k][j]
                
            listaAux.append(soma)
        
        matrizC.append(listaAux)
    
    return matrizC

if __name__ == "__main__":

    eh_loop: bool = True

    matrizA: list[list[int]] = []
    matrizB: list[list[int]] = []
    matrizC: list[list[int]] = []
    

    while eh_loop:

        
        opcao = int(input("Digite sua opção\n1) Gerar Matrizes\n2) Mostrar Matrizes\n3) Multiplicar Matrizes\n4) Sair\nOpção: "))

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
        elif opcao == 3:
            matrizC = multiplicaMatriz(matrizA, matrizB)
            
            print("\nMatriz A:")
            mostraMatriz(matrizA)

            print("\nMatriz B:")
            mostraMatriz(matrizB)

            print("\nResultado da multiplicação (A x B):")
            mostraMatriz(matrizC)
        
        elif opcao == 4:
            
            eh_loop = False
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")