from copy import deepcopy
from dataclasses import dataclass

from filaDinamica import *


class PilhaComFila:
    def __init__(self):
        self._entrada: FilaDinamica = FilaDinamica()

        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def empilha(self, item: TipoItem) -> bool:
        self._entrada.enfileira(item)
        self._numItens += 1

        return True

    def desempilha(self) -> bool:
        if self.vazia():
            return False

        for i in range(self._numItens - 1):
            item = self._entrada.primeiro()
            self._entrada.desenfileira()
            self._entrada.enfileira(item)

        self._entrada.desenfileira()
        self._numItens -= 1

        return True

    def topo(self) -> TipoItem | None:
        if self.vazia():
            return False

        for i in range(self._numItens - 1):
            item = self._entrada.primeiro()
            self._entrada.desenfileira()
            self._entrada.enfileira(item)

        item = self._entrada.primeiro()
        self._entrada.desenfileira()
        self._entrada.enfileira(item)

        return deepcopy(item)

    def mostra(self) -> None:
        if self.vazia():
            print("Pilha vazia")
            return

        filaAuxiliar = FilaDinamica()

        for _ in range(self._numItens):
            item = self._entrada.primeiro()
            self._entrada.desenfileira()
            self._entrada.enfileira(item)
            filaAuxiliar.enfileira(item)

        print("Topo -> ", end="")

        for restantes in range(self._numItens, 0, -1):

            for _ in range(restantes - 1):
                item = filaAuxiliar.primeiro()
                filaAuxiliar.desenfileira()
                filaAuxiliar.enfileira(item)

            item = filaAuxiliar.primeiro()
            filaAuxiliar.desenfileira()

            print(item.valor, end="")

            if restantes > 1:
                print(", ", end="")

        print(" <- Fim")

    def esvazia(self) -> None:
        self._entrada = None
        self._numItens -= 1