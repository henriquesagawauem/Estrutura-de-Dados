import random

def gerarVetor(n: int) -> list[int]:
    lista = []
    for i in range(n):
        num = random.randint(0, 10)
        lista.append(num)

    return lista

def produtoEscalarWhile(v1: list[int], v2: list[int], n: int) -> int:
    soma = 0

    i = 0
    while i < n:
        temp = v1[i] * v2[i]
        soma = soma + temp

        i += 1

    return soma

def produtoEscalarFor(v1: list[int], v2: list[int], n: int) -> int:
    soma = 0

    for i in range(n):
        temp = v1[i] * v2[i]
        soma = soma + temp

    return soma

def produtoEscalarRec(v1: list[int], v2: list[int], n: int) -> int:
    soma = 0

    if n == 0:
        soma = 0
    else:
        soma = (v1[n - 1] * v2[n - 1]) + produtoEscalarRec(v1, v2, n - 1)

    return soma

if __name__ == "__main__":
    eh_loop = True

    while eh_loop:
        num = int(input("Pense em um número e digite: "))

        v1 = gerarVetor(num)
        v2 = gerarVetor(num)

        print("Calculando o produto escalar de " + str(v1) + " e " + str(v2))

        print("Produto escalar com While: ")
        print(produtoEscalarWhile(v1, v2, num))

        print("Produto escalar com For: ")
        print(produtoEscalarFor(v1, v2, num))

        print("Produto escalar com recursividade: ")
        print(produtoEscalarRec(v1, v2, num))

        resposta = int(input(("Quer continuar?\n1 - Sim\n0 - Não\n")))
        if resposta != 1:
            eh_loop = False
            print("Encerrando o programa :)")
