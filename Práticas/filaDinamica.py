from dataclasses import dataclass
from copy import deepcopy

@dataclass
class TipoItem:
    valor: None | str | int | float = None

class TipoNo:
    item: TipoItem
    _prox: "TipoNo | None" = None

class FilaDinamica:
    def __init__(self):
        self._inicio = None
        self._ultimo = None
        self._numItens = 0
        self.item = None

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return False

    def enfileira(self, item: TipoItem) -> bool:
        novoNo = TipoNo()
        novoNo.item = deepcopy(item)
        if self.vazia():
            self._inicio = novoNo
            self._ultimo = novoNo
        else:
            self._ultimo._prox = novoNo
            self._ultimo = novoNo

        self._numItens += 1

        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            return False

        self._inicio = self._inicio._prox
        self._numItens -= 1
        if self.vazia():
            self._ultimo = None
        return True

    def itemPrimeiro(self) -> TipoItem:
        return deepcopy(self._inicio.item)
    

    def mostra(self) -> None:
        if self.vazia():
            print("Fila vázia")
        else:
            aux = self._inicio
            while aux != None:
                print(aux.item.valor)
                aux = aux._prox

    def esvazia(self) -> None:
        self._inicio = None
        self._ultimo = None
        self._numItens = 0
        self.item = None


p = FilaDinamica()

p.enfileira(TipoItem(valor=1))
p.enfileira(TipoItem(valor=3))
p.enfileira(TipoItem(valor=10))

p.mostra()

print()

p.desenfileira()
p.desenfileira()

p.mostra()

print()

p.enfileira(TipoItem(valor=50))

p.mostra()

print(p.itemPrimeiro())

print()


p.esvazia()

p.mostra()