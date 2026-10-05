from __future__ import annotations

import os
import random
import string
import time
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    valor: object | None = None


class FilaEstatica:
    """Fila estática circular."""

    def __init__(self, maxTam: int):
        self._maxTam: int = maxTam
        self._fila: list[TipoItem | None] = [None for _ in range(maxTam)]
        self._posPrimeiro: int = 0
        self._posUltimo: int = -1
        self._numItens: int = 0
        self.item: TipoItem | None = None

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._maxTam

    def enfileira(self, item: TipoItem) -> bool:
        if self.cheia():
            return False

        self._posUltimo = (self._posUltimo + 1) % self._maxTam
        self._fila[self._posUltimo] = deepcopy(item)
        self._numItens += 1
        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            self.item = None
            return False

        item = self._fila[self._posPrimeiro]
        self._fila[self._posPrimeiro] = None
        self._posPrimeiro = (self._posPrimeiro + 1) % self._maxTam
        self._numItens -= 1
        self.item = deepcopy(item)
        return True

    def itemPrimeiro(self) -> TipoItem | None:
        if self.vazia():
            return None

        item = self._fila[self._posPrimeiro]
        return deepcopy(item)

    def mostra(self) -> None:
        if self.vazia():
            print("\nSituação da Fila: Vazia!")
            return

        print("\nSituação da Fila: ", end="")
        pos = self._posPrimeiro

        for i in range(self._numItens):
            item = self._fila[pos]
            print(item.valor, end="" if i == self._numItens - 1 else ", ")
            pos = (pos + 1) % self._maxTam

        print("\n")

    def esvazia(self) -> None:
        self._fila = [None for _ in range(self._maxTam)]
        self._posPrimeiro = 0
        self._posUltimo = -1
        self._numItens = 0
        self.item = None


@dataclass
class _TipoNo:
    item: TipoItem | None = None
    _prox: _TipoNo | None = None


class FilaDinamica:
    """Fila dinâmica encadeada."""

    def __init__(self, maxTam: int | None = None):
        self._maxTam: int | None = maxTam
        self._primeiro: _TipoNo | None = None
        self._ultimo: _TipoNo | None = None
        self._numItens: int = 0
        self.item: TipoItem | None = None

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._maxTam is not None and self._numItens >= self._maxTam

    def enfileira(self, item: TipoItem) -> bool:
        if self.cheia():
            return False

        novoNo = _TipoNo(item=deepcopy(item))

        if self.vazia():
            self._primeiro = novoNo
            self._ultimo = novoNo
        else:
            self._ultimo._prox = novoNo
            self._ultimo = novoNo

        self._numItens += 1
        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            self.item = None
            return False

        aux = self._primeiro
        self._primeiro = self._primeiro._prox
        self.item = deepcopy(aux.item)
        aux._prox = None
        self._numItens -= 1

        if self.vazia():
            self._ultimo = None

        return True

    def itemPrimeiro(self) -> TipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._primeiro.item)

    def mostra(self) -> None:
        if self.vazia():
            print("\nSituação da Fila: Vazia!")
            return

        print("\nSituação da Fila: ", end="")
        atual = self._primeiro

        while atual is not None:
            print(atual.item.valor, end="" if atual._prox is None else ", ")
            atual = atual._prox

        print("\n")

    def esvazia(self) -> None:
        self._primeiro = None
        self._ultimo = None
        self._numItens = 0
        self.item = None


@dataclass
class Cliente:
    nome: str
    tempo_atendimento: int

    def __str__(self) -> str:
        return self.nome


def limparTela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def criarCliente(tempoMaxAtendimento: int) -> Cliente:
    nome = random.choice(string.ascii_uppercase)
    tempo = random.randint(1, tempoMaxAtendimento)
    return Cliente(nome, tempo)


def main() -> None:
    print("=== SIMULADOR DE FILA BANCÁRIA ===")

    tempoSimulacao = int(input("Quantidade de ciclos da simulação: "))
    tamMaxFila = int(input("Tamanho máximo da fila: "))
    probabilidade = float(input("Probabilidade de chegada de um cliente (%): "))
    tempoMaxAtendimento = int(input("Tempo máximo de atendimento: "))

    print("\nTipo da fila:")
    print("1 - Fila Estática Circular")
    print("2 - Fila Dinâmica")

    tipoFila = int(input("Escolha: "))

    if tipoFila == 1:
        fila = FilaEstatica(tamMaxFila)
    elif tipoFila == 2:
        fila = FilaDinamica(tamMaxFila)
    else:
        print("Tipo de fila inválido.")
        return

    quantidadeFila = 0

    clienteCaixa: Cliente | None = None
    tempoRestante = 0

    totalClientes = 0
    totalAtendidos = 0
    totalRecusados = 0

    for ciclo in range(1, tempoSimulacao + 1):
        mensagem = ""

        sorteio = random.random() * 100

        if sorteio < probabilidade:
            if quantidadeFila < tamMaxFila:
                cliente = criarCliente(tempoMaxAtendimento)
                item = TipoItem(cliente)

                if fila.enfileira(item):
                    quantidadeFila += 1
                    totalClientes += 1
                    mensagem = f"Cliente {cliente.nome} entrou na fila."
            else:
                totalRecusados += 1
                mensagem = "Um cliente chegou, mas a fila estava cheia."

        if clienteCaixa is None and not fila.vazia():
            primeiro = fila.itemPrimeiro()

            if primeiro is not None:
                clienteCaixa = primeiro.valor
                tempoRestante = clienteCaixa.tempo_atendimento

        limparTela()

        print("==============================")
        print("      FILA BANCÁRIA")
        print("==============================")

        print(f"\nCiclo: {ciclo}/{tempoSimulacao}")
        print(f"\nQuantidade na fila: {quantidadeFila}/{tamMaxFila}")

        fila.mostra()

        print("Caixa:")

        if clienteCaixa is None:
            print("Caixa livre")
        else:
            print(f"Cliente: {clienteCaixa.nome}")
            print(f"Tempo restante: {tempoRestante}")

        if mensagem:
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

    print(f"\nClientes que entraram: {totalClientes}")
    print(f"Clientes atendidos: {totalAtendidos}")
    print(f"Clientes ainda na fila: {quantidadeFila}")
    print(f"Clientes recusados: {totalRecusados}")

    print("\nSituação final:")
    fila.mostra()


if __name__ == "__main__":
    main()
