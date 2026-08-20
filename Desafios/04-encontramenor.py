import random

def gerarVetor(tamanho: int) -> list[int]:
    vetor: list[int] = []

    for i in range(tamanho):
        vetor.append(random.randint(0, 9))

    return vetor

def lerVetor(tamanho, mensagem):
    print(mensagem)
    lista = []
    for i in range(tamanho):
        valor = int(input("Elemento " + str(i + 1) + ": "))
        lista.append(valor)
    return lista

def encontraPrimeira(vetorMenor: list[int], vetorMaior: list[int]) -> int:
    if len(vetorMenor) > len(vetorMaior):
        return -1

    posicao = -1

    limite = len(vetorMaior) - len(vetorMenor)

    for i in range(limite + 1):
        encontrou = True

        for j in range(len(vetorMenor)):
            if vetorMaior[i + j] != vetorMenor[j]:
                encontrou = False

        if encontrou and posicao == -1:
            posicao = i

    return posicao

def confereOcorrencia(vetorMenor: list[int], vetorMaior: list[int], m: int, i: int) -> bool:
    confere = True
    j = 0
    while j < m and confere:
        if vetorMaior[i + j] != vetorMenor[j]:
            confere = False
        j += 1
    return confere

def encontraTodas(vetorMenor: list[int], vetorMaior: list[int], n: int, m: int) -> list[int]:
    posicoes = []

    i = 0
    while i <= n - m:
        if confereOcorrencia(vetorMenor, vetorMaior, m, i):
            posicoes.append(i)
        i += 1
    return posicoes

def removerTodas(vetorMenor: list[int], vetorMaior: list[int]) -> list[int]:
    i = 0
    
    while i <= len(vetorMaior) - len(vetorMenor):
        if confereOcorrencia(vetorMenor, vetorMaior, len(vetorMenor), i):
            for j in range(len(vetorMenor)):
                for k in range(i, len(vetorMaior) - 1):
                    vetorMaior[k] = vetorMaior[k + 1]
                
                vetorMaior.pop()
        else:
            i += 1
    
    return vetorMaior

def substituirTodas(vetorMenor: list[int], vetorMaior: list[int], vetorNovo: list[int]):
    i = 0
    
    while i <= len(vetorMaior) - len(vetorMenor):
        if confereOcorrencia(vetorMenor, vetorMaior, len(vetorMenor), i):
            
            for j in range(len(vetorMenor)):
                vetorMaior[i + j] = vetorNovo[j]
            i += len(vetorMenor)
        else:
            i += 1
    
    return vetorMaior


if __name__ == "__main__":

    n = 10
    m = 5

    vetorMaior = gerarVetor(n)

    print("Vetor maior:", vetorMaior)

    continuar = True

    while continuar:
        opcao = int(input("Escolha uma opção:\n1) Configurar n e m\n2) Localizar todas as ocorrências\n3) remover todas as ocorrências\n4) Substituir todas as ocorrências\n5) Sair\nOpção escolhida: "))

        if opcao == 1:
            n = int(input("Digite o valor de n: "))
            m = int(input("Digite o valor de m: "))

            while m > n:
                m = int(input("Erro: m deve ser menor ou igual a n\nDigite novamente o valor de m: "))

            vetorMaior = gerarVetor(n)
            print("Vetor maior gerado: ", vetorMaior)

            vetorMenor = lerVetor(m, "Digite os elementos do vetor menor:")
            print("Vetor menor gerado: ", vetorMenor)

        elif opcao == 2:

            print("Vetor maior: ", vetorMaior)
            vetorMenor = lerVetor(m, "Digite o vetor menor: ")

            posicoes = encontraTodas(vetorMenor, vetorMaior, n, m)
            
            if len(posicoes) > 0:
                print("Lista menor encontrada nas posições:")
                for i in range(len(posicoes)):
                    print(posicoes[i], end=" ")
                print()
            else:
                print("O vetor menor não foi encontrado.")

        elif opcao == 3:
            print("Vetor maior: ", vetorMaior)
            vetorMenor = lerVetor(m, "Digite o vetor menor:")
            vetorMaior = removerTodas(vetorMenor, vetorMaior)
            n = len(vetorMaior)
            print("Vetor maior após a remoção: ", vetorMaior)
        
        elif opcao == 4:
            print("Vetor maior: ", vetorMaior)
            vetorMenor = lerVetor(m, "Digite o vetor menor:")
            vetorNovo = lerVetor(m, "Digite os elementos do novo vetor: ")
            vetorMaior = substituirTodas(vetorMenor, vetorMaior, vetorNovo)
            print("Vetor alterado com sucesso: ", vetorMaior)
        
        elif opcao == 5:
            continuar = False
            print("Encerrando o programa :(")
        else:
            print("Opção inválida. Tente novamente")