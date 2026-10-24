from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    valor: int | float | str | None = None


@dataclass
class TipoNo:
    item: TipoItem | None = None
    _prox: "TipoNo | None" = None


class PilhaDinamica:
    def __init__(self):
        self._topo: TipoNo | None = None
        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def empilha(self, item: TipoItem) -> bool:
        novoNo = TipoNo(item=item, _prox=self._topo)
        self._topo = novoNo
        self._numItens += 1

        return True

    def desempilha(self) -> bool:
        if self.vazia():
            return False

        self._topo = self._topo._prox
        self._numItens -= 1

        return True

    def topo(self) -> TipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._topo.item)

    def mostra(self) -> None:
        if self.vazia():
            print("Pilha vázia")
            return

        aux = self._topo
        print("Topo -> ", end="")
        for i in range(self._numItens - 1):
            print(aux.item.valor, end=", ")
            aux = aux._prox

        print(aux.item.valor, end=" <- Fim\n")
        return

    def esvazia(self) -> None:
        self._topo = None
        self._numItens = 0