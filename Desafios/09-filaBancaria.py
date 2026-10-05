import os
import random
import time
from dataclasses import dataclass
import string

from filaEstaticaCircular import (
    filaEstDin as FilaEstatica,
    tipoItem as ItemEstatico
)

from filaDinamica import (
    filaEstDin as FilaDinamica,
    tipoItem as ItemDinamico
)


@dataclass
class Cliente:
    nome: str
    tempo_atendimento: int

    def __str__(self):
        return self.nome

def limparTela():
    os.system("cls" if os.name == "nt" else "clear")

def criarCliente() -> Cliente:
    nome = random.choice(string.ascii_uppercase)
    tempo = random.randint(1, tempoMaxAtendimento)

    return Cliente(nome, tempo)

print("=== SIMULADOR DE FILA BANCÁRIA ===")
tempoSimulacao = int(
    input("Quantidade de ciclos da simulação: ")
)

tamMaxFila = int(
    input("Tamanho máximo da fila: ")
)

probabilidade = float(
    input("Probabilidade de chegada de um cliente (%): ")
)

tempoMaxAtendimento = int(
    input("Tempo máximo de atendimento: ")
)

print("\nTipo da fila:")
print("1 - Fila Estática Circular")
print("2 - Fila Dinâmica")

tipoFila = int(input("Escolha: "))

if tipoFila == 1:
    fila = FilaEstatica(tamMaxFila)
    TipoItem = ItemEstatico
else:
    fila = FilaDinamica(tamMaxFila)
    TipoItem = ItemDinamico


quantidadeFila = 0

clienteCaixa = None
tempoRestante = 0

totalClientes = 0
totalAtendidos = 0
totalRecusados = 0

for ciclo in range(1, tempoSimulacao + 1):

    mensagem = ""

    sorteio = random.random() * 100

    if sorteio < probabilidade:

        if quantidadeFila < tamMaxFila:
            cliente = criarCliente()
            item = TipoItem(cliente)

            if fila.enfileira(item):

                quantidadeFila += 1
                totalClientes += 1

                mensagem = f"Cliente {cliente.nome} entrou na fila."
        else:


            totalRecusados += 1

            mensagem = f"Um cliente chegou mas a fila estava cheia."

    if clienteCaixa is None and not fila.vazia():
        primeiro = fila.itemPrimeiro()
        clienteCaixa = primeiro.valor
        tempoRestante = clienteCaixa.tempo_atendimento

    limparTela()

    print("==============================")
    print("      FILA BANCÁRIA")
    print("==============================")

    print(
        f"\nCiclo: {ciclo}/{tempoSimulacao}"
    )

    print(
        f"\nQuantidade na fila: "
        f"{quantidadeFila}/{tamMaxFila}"
    )

    fila.mostra()

    print("\nCaixa:")

    if clienteCaixa is None:
        print("Caixa livre")
    else:
        print(f"Cliente: {clienteCaixa.nome}")

        print(
            f"Tempo restante: {tempoRestante}"
        )

    if mensagem != "":
        print(f"\n{mensagem}")

    if clienteCaixa is not None:
        tempoRestante -= 1

        if tempoRestante == 0:
            fila.desenfileira()

            quantidadeFila -= 1
            totalAtendidos += 1

            clienteCaixa = None

    time.sleep(1)

limparTela()

print("==============================")
print("       FIM DA SIMULAÇÃO")
print("==============================")

print(
    f"\nClientes que entraram: "
    f"{totalClientes}"
)

print(
    f"Clientes atendidos: "
    f"{totalAtendidos}"
)

print(
    f"Clientes ainda na fila: "
    f"{quantidadeFila}"
)

print(
    f"Clientes recusados: "
    f"{totalRecusados}"
)

print("\nSituação final:")

fila.mostra()