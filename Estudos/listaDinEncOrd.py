from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    nome: str = ""
    idade: int = 0
    cpf: str = ""

@dataclass
class TipoNo:
    item: TipoItem = TipoItem
    _prox: "TipoNo | None" = None

class ListaDinEncOrd:
    def __init__(self):
        self._inicio: TipoNo | None = None
        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def inserir(self, item: TipoItem) -> bool:
        novoNo = TipoNo(item=item)

        if self.vazia() or item.nome < self._inicio.item.nome:
            novoNo._prox = self._inicio
            self._inicio = novoNo
        else:
            anterior = None
            atual = self._inicio

            while atual != None and atual.item.nome <= item.nome:
                anterior = atual
                atual = atual._prox

            anterior._prox = novoNo
            novoNo._prox = atual

        self._numItens += 1
        return True

    def remover(self, nome: str) -> bool:
        if self.vazia():
            return False

        anterior = None
        atual = self._inicio

        while atual != None and atual.item.nome != nome:
            anterior = atual
            atual = atual._prox

        if atual == None or atual.item.nome != nome:
            return False

        if anterior == None:
            self._inicio = self._inicio._prox
        else:
            anterior._prox = atual._prox

        self._numItens -= 1

        return True

    def consultar(self, nome: str) -> TipoItem | None:
        if self.vazia():
            return None

        atual = self._inicio
        for i in range(self._numItens):
            if atual.item.nome == nome:
                return deepcopy(atual.item)
            atual = atual._prox

        return None

    def atualizar(self, item: TipoItem) -> bool:
        if self.vazia():
            return False

        atual = self._inicio

        for i in range(self._numItens):
            if atual.item.nome == item.nome:
                self.remover(item.nome)
                self.inserir(item)
                return True
            atual = atual._prox
        return False

    def mostrar(self) -> None:
        if self.vazia():
            print("Lista vázia!")
            return
        else:
            aux = self._inicio

            for i in range(self._numItens - 1):
                print(aux.item.nome, end=", ")
                aux = aux._prox

            print(aux.item.nome, end="\n")

        return

    def esvazia(self) -> None:
        self._inicio = None
        self._numItens = 0

lista = ListaDinEncOrd()

lista.inserir(TipoItem("Palmeiras"))
lista.inserir(TipoItem("Flamengo"))
lista.inserir(TipoItem("Santos"))
lista.inserir(TipoItem("Atlhetico-PR"))

lista.mostrar()