from dataclasses import dataclass
from copy import deepcopy

_TERRA: int = -1

@dataclass
class tipoItem:
    valor: int | float | None | str = None

class filaEstDin():
    def __init__(self, tamMax: int):
        self._inicio: int = 0
        self._fim: int = _TERRA
        self._fila: list[tipoItem]= [None for i in range(tamMax)]
        self._nItens: int = 0
        self.item: tipoItem = tipoItem()
        self._tamMax: int = tamMax

    def vazia(self) -> bool:
        return self._nItens == 0

    def cheia(self) -> bool:
        return self._nItens == self._tamMax

    def enfileira(self, item: tipoItem) -> bool:
        if self.cheia():
            return False

        self._fim = (self._fim + 1) % self._tamMax
        self._fila[self._fim] = deepcopy(item)
        self._nItens += 1
        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            return False

        self.item = deepcopy(self._fila[self._inicio])
        self._inicio = (self._inicio + 1) % self._tamMax
        self._nItens -= 1
        return True


    def itemPrimeiro(self) -> tipoItem:
        if self.vazia():
            return tipoItem()

        return deepcopy(self._fila[self._inicio])

    def mostra(self) -> None:
        if self.vazia():
            print("Fila vázia")
        else:
            print("Elementos da fila: \n")
            aux = self._inicio
            quantidade = self._nItens
            while quantidade > 0:
                separador = ", " if quantidade > 1 else "\n"
                print(self._fila[aux], separador, sep='', end='')
                
                aux = (aux + 1) % self._tamMax
                quantidade -= 1
                



    def esvazia(self) -> None:
        self._inicio = 0
        self._fim = _TERRA
        self._nItens = 0
        self.item = tipoItem