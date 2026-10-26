from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    nome: str = ""
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
        novoNo: TipoNo = TipoNo(item=item)

        if self.vazia() or novoNo.item.nome < self._inicio.item.nome:
            novoNo._prox = self._inicio
            self._inicio = novoNo
        else:
            anterior = None
            atual = self._inicio

            while atual != None and atual.item.nome <= item.nome:
                anterior = atual
                atual = atual._prox

            if atual != None and atual.item.nome == item.nome:
                return False

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

        while atual != None and atual.item.nome != nome:
            atual = atual._prox

        if atual == None or atual.item.nome != nome:
            return None

        return deepcopy(atual.item)

    def atualizar(self, item: TipoItem) -> bool:
        if self.vazia():
            return False

        atual = self._inicio
    
        while atual != None and atual.item.nome != item.nome:
            atual = atual._prox
    
        if atual == None or atual.item.nome != item.nome:
            return False

        self.remover(item.nome)
        self.inserir(item)
        return True

    def mostrar(self) -> None:
        if self.vazia():
            print("Lista vázia!")
            return

        aux = self._inicio

        for i in range(self._numItens):
            print(aux.item.nome, end=" ")
            aux = aux._prox

        return

    def esvazia(self) -> None:
        self._inicio = None
        self._numItens = 0

    def reordenaCpf(self) -> bool:
        inicioOrdenado = None
        atual = self._inicio

        for i in range(self._numItens):
            proximo = atual._prox

            if inicioOrdenado == None or atual.item.cpf <= inicioOrdenado.item.cpf:
                atual._prox = inicioOrdenado
                inicioOrdenado = atual
            else:
                anterior = inicioOrdenado

                while anterior._prox != None and anterior._prox.item.cpf <= atual.item.cpf:
                    anterior = anterior._prox

                atual._prox = anterior._prox
                anterior._prox = atual
            atual = proximo
        self._inicio = inicioOrdenado

    def inverter(self) -> None:
        if self.vazia():
            return

        anterior = None
        atual = self._inicio

        while atual != None:
            proximo = atual._prox
            atual._prox = anterior
            anterior = atual
            atual = proximo

        self._inicio = anterior