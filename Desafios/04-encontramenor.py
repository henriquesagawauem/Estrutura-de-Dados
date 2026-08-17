import random

def gerarVetor(tam: int) -> list[int]:
    vetor = []

    for _ in range(tam):
        vetor.append(random.randint(0, 99))

    return vetor

def encontraMenor(vetorMenor: list[int], vetorMaior: list[int]) -> int:
    if len(vetorMenor) == len(vetorMaior):
        return 0
    
    contador = 0

    for i in range(len(vetorMaior)):
        if len(vetorMenor) < i:
            return -1
        if vetorMaior[i] == vetorMenor[i]:
            eh_igual = True
            contador += 1

            if contador == len(vetorMenor):
                return i - len(vetorMenor)
        else:
            contador = 0
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

            if (dig != -1):
                vetorMenor.append(dig)
            else:
                digitando = False
        
        resultado = encontraMenor(vetorMenor, vetorMaior)
        if (resultado == -1):
            print("Lista não encontrada")
        else:
            print(f"Lista encontrada em: {resultado}")
