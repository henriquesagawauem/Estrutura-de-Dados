from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    valor: int | float | str | None = None

_TERRA: int = -1

class PilhaEstatica:
    def __init__(self, tamMax: int):
        self._tamMax: int = tamMax
        self._topo: int = -1
        self._pilha: list[TipoItem] = [TipoItem() for i in range(tamMax)]
        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._tamMax

    def empilha(self, item: TipoItem) -> bool:
        if self.cheia():
            return False

        self._topo += 1
        self._pilha[self._topo] = deepcopy(item)
        self._numItens += 1

        return True

    def desempilha(self) -> bool:
        if self.vazia():
            return False

        self._topo -= 1
        self._numItens -= 1

        return True

    def topo(self) -> TipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._pilha[self._topo])

    def mostra(self) -> None:
        if self.vazia():
            print("Pilha vázia")
            return
        print("Topo -> ", end="")
        for i in range(self._numItens - 1):
            print(self._pilha[self._topo - i].valor, end=", ")

        print(self._pilha[0].valor, end=" <- Fim\n")
        return

    def esvazia(self) -> None:
        self._topo = _TERRA
        self._numItens = 0