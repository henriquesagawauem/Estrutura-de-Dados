import random

def gerarVetor(tam: int) -> list[int]:
    vetor = []

    for _ in range(tam):
        vetor.append(random.randint(0, 99))

    return vetor

def encontraMenor(vetorMenor: list[int], vetorMaior: list[int]) -> int:
    if len(vetorMenor) > len(vetorMaior) or len(vetorMenor) == 0 or len(vetorMaior) == 0:
        return -1

    for i in range(len(vetorMaior)):
        contador = 0
        j = i
        continuar = True

        while j < len(vetorMaior) and continuar and contador < len(vetorMenor):
            if vetorMaior[j] == vetorMenor[contador]:
                contador += 1
                j += 1
            else:
                continuar = False

        if contador == len(vetorMenor):
            return i
    return -1


if __name__ == "__main__":
    eh_loop: bool = True
    
    while eh_loop:
        tamMaior = int(input("Digite o tamanho do vetor maior: "))
        vetorMaior = gerarVetor(tamMaior)

        print(f"Vetor gerado: {vetorMaior}")

        digitando = True
        vetorMenor = []
        while digitando:
            dig = int(input("Digite um valor para a lista menor\nDigite -1 para parar\nDígito: "))

            if (dig >= 0):
                vetorMenor.append(dig)
            else:
                digitando = False
        
        resultado = encontraMenor(vetorMenor, vetorMaior)
        if (resultado == -1):
            print("Lista não encontrada")
        else:
            print(f"Lista {vetorMenor} encontrada no índice: {resultado}")

        resposta = input("Deseja continuar?\n1 - Sim\n2 - Não\nDigite: ")

        if (resposta == "2"):
            eh_loop = False
            print("Encerrando o programa :(")
