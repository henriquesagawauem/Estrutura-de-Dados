from copy import deepcopy
from dataclasses import dataclass

from pilhaDinamica import *


class FilaComPilha:
    def __init__(self):
        self._entrada: PilhaDinamica = PilhaDinamica()

        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def enfileira(self, item: TipoItem) -> bool:
        self._entrada.empilha(item)
        self._numItens += 1

        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            return False

        self._desenfileiraAuxiliar(self._entrada)
        self._numItens -= 1
        return True

    def _desenfileiraAuxiliar(self, pilha: PilhaDinamica | None) -> PilhaDinamica:
        item = pilha.topo()
        pilha.desempilha()

        if pilha.vazia():
            return

        self._desenfileiraAuxiliar(pilha)
        pilha.empilha(item)

    def mostra(self) -> None:
        if self.vazia():
            print("Fila vazia")
            return

        print("Início -> ", end="")
        self._mostraAuxiliar(self._entrada)
        print("<- Fim")

    def _mostraAuxiliar(self, pilha: PilhaDinamica) -> None:
        if pilha.vazia():
            return

        item = pilha.topo()
        pilha.desempilha()

        self._mostraAuxiliar(pilha)

        print(item.valor, end=" ")
        pilha.empilha(item)

    def primeiro(self) -> TipoItem | None:
        if self.vazia():
            return None

        item = self._entrada.topo()
        self._desenfileiraAuxiliar(self._entrada)
        self._entrada.empilha(item)

        return deepcopy(item)

    def esvazia(self) -> None:
        self._entrada.esvazia()
        self._numItens = 0