# Desafio da aula do dia 11/08/2026

def fatorialWhile(n):
    fatorial = 1

    while (n > 0):
        fatorial = fatorial * n
        n -= 1

    return fatorial
    

def fatorialFor(n):
    fatorial = 1

    for i in range(1, n + 1):
        fatorial = fatorial * i

    return fatorial

def fatorialRec(n):
    fatorial = 1

    if n > 1:
        fatorial = n * fatorialRec(n - 1)

    return fatorial

if __name__ == "__main__":

    eh_loop = True

    while eh_loop:
        num = int(input("Digite um número: "))

        print(f"Fatorial usando while: {fatorialWhile(num)}")
        
        print(f"Fatorial usando for: {fatorialFor(num)}")
        
        print(f"Fatorial usando recursividade: {fatorialRec(num)}")

        resposta = int(input("Você quer executar mais uma vez?\n1 - Sim\n2 - Não\nResposta: "))

        if resposta == 2:
            eh_loop = False
            print("Encerrando o programa :)")