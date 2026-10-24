from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    valor: int | float | str | None = None


@dataclass
class TipoNo:
    item: TipoItem | None = None
    _prox: "TipoNo | None" = None


class FilaDinamica:
    def __init__(self):
        self._inicio: TipoNo = None
        self._fim: TipoNo = None
        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def enfileira(self, item: TipoItem) -> bool:
        novoNo: TipoNo = TipoNo(item=deepcopy(item))

        if self.vazia():
            self._inicio = novoNo
            self._fim = novoNo
        else:
            self._fim._prox = novoNo
            self._fim = novoNo

        self._numItens += 1

        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            return False

        self._inicio = self._inicio._prox
        self._numItens -= 1

        return True

    def primeiro(self) -> TipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._inicio.item)

    def mostra(self) -> None:
        if self.vazia():
            print("Fila vázia!")
            return

        aux = self._inicio

        print("Início -> ", end="")
        for i in range(self._numItens - 1):
            print(aux.item.valor, end=", ")
            aux = aux._prox

        print(aux.item.valor, end=" <- Fim")
        return

    def esvazia(self) -> None:
        self._inicio: TipoNo = None
        self._fim: TipoNo = None
        self._numItens: int = 0
