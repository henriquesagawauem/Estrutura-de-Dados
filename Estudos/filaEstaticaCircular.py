from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    valor: int | float | str | None = None

class FilaEstaticaCircular:
    def __init__(self, tamMax: int):
        self._tamMax: int = tamMax
        self._inicio: int = 0
        self._fim: int = -1
        self._fila: list[TipoItem] = [TipoItem() for i in range(tamMax)]
        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._tamMax

    def enfileira(self, item: TipoItem) -> bool:
        if self.cheia():
            return False

        self._fim = (self._fim + 1) % self._tamMax
        self._fila[self._fim] = deepcopy(item)
        self._numItens += 1
        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            return None

        self._inicio = (self._inicio + 1) % self._tamMax
        self._numItens -= 1

        return True

    def primeiro(self) -> TipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._fila[self._inicio])

    def mostra(self) -> None:
        if self.vazia():
            print("Fila vázia!")
            return

        print("Início -> ", end="")
        for i in range(self._numItens - 1):
            print(self._fila[(self._inicio + i) % self._tamMax].valor, end=", ")

        print(self._fila[self._fim].valor, end=" <- Fim")
        return

    def esvazia(self) -> None:
        self._inicio: int = 0
        self._fim: int = -1
        self._numItens: int = 0