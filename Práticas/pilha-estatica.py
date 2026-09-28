from dataclasses import dataclass
from copy import deepcopy

@dataclass
class TipoItem:
    valor: int | float | None | str = None

class Pilha:
    def __init__(self, tamMax: int) -> None:
        self._pilha: list[TipoItem] = [TipoItem() for i in range(tamMax)]
        self._tamMax: int = tamMax
        self._topo: int = -1
        self.rem: TipoItem = TipoItem()


    def vazia(self) -> bool:
        return self._topo == -1

    def cheia(self) -> bool:
        return self.topo == self._tamMax - 1

    def empilha(self, item: TipoItem) -> bool:
        if self.cheia():
            return False
        else:
            self._topo += 1
            self._pilha[self._topo] = deepcopy(item)
            return True

    def desempilha(self) -> bool:
        if self.vazia():
            return False
        else:
            self.rem = deepcopy(self._pilha[self._topo])
            self._topo -= 1
            return True

    def topo(self) -> TipoItem:
        if self.vazia():
            return TipoItem()
        else:
            return deepcopy(self._pilha[self._topo])

    def mostra(self, text: str) -> None:
        if self.vazia():
            print("Pilha vázia :(")
        else:
            print("Pilha: ")
            for i in range(self._topo + 1, -1, -1):
                print(self._pilha[i].valor)
    
    def esvazia(self) -> None:
        self._topo = -1
        self.rem = TipoItem()