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
    _prox: int = 0

_TERRA: int = -1

class ListaEstaticaEncadeada:
    def __init__(self, tamMax: int):
        self._tamMax: int = tamMax
        self._inicio: int = _TERRA
        self._lista: list[TipoNo] = [TipoNo() for i in range(tamMax)]
        self._livres: int = 0 if tamMax > 0 else _TERRA
        self._numItens: int = 0
        self.item: TipoItem | None = None

        for i in range(tamMax - 1):
            self._lista[i]._prox = i + 1

        if tamMax > 0:
            self._lista[tamMax - 1]._prox = _TERRA

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._tamMax

    def _buscaAnterior(self, nome: str) -> int:
        anterior = _TERRA
        atual = self._inicio

        while atual != _TERRA and self._lista[atual].item.nome < nome:
            anterior = atual
            atual = self._lista[atual]._prox

        return anterior

    def inserir(self, item: TipoItem) -> bool:
        if self.cheia():
            return False

        anterior = self._buscaAnterior(item.nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior]._prox

        if atual != _TERRA and self._lista[atual].item.nome <= item.nome:
            return False

        novaPosicao: int = self._livres
        self._livres = self._lista[novaPosicao]._prox

        self._lista[novaPosicao].item = deepcopy(item)
        self._lista[novaPosicao]._prox = atual

        if anterior == _TERRA:
            self._inicio = novaPosicao
        else:
            self._lista[anterior]._prox = novaPosicao

        self._numItens += 1

        return True

    def remover(self, nome: str) -> bool:
        if self.vazia():
            return False

        anterior = self._buscaAnterior(nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior]._prox

        if atual == _TERRA or self._lista[atual].item.nome != nome:
            return False

        self.item = self._lista[atual].item

        if anterior == _TERRA:
            self._inicio = self._lista[atual]._prox
        else:
            self._lista[anterior]._prox = self._lista[atual]._prox

        self._lista[atual]._prox = self._livres
        self._livres = atual

        self._numItens -= 1

        return True

    def consultar(self, nome: str) -> TipoItem | None:
        if self.vazia():
            return None

        atual = self._inicio

        for i in range(self._numItens):
            if self._lista[atual].item.nome == nome:
                return deepcopy(self._lista[atual].item)

            atual = self._lista[atual]._prox

        return None

    def atualizar(self, item: TipoItem) -> bool:
        if self.vazia():
            return False

        anterior = self._buscaAnterior(item.nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior]._prox
        
        if atual == _TERRA or self._lista[atual].item.nome != item.nome:
            return False

        self.remover(item.nome)
        self.inserir(item)

        return True

    def mostrar(self) -> None:
        if self.vazia():
            print("Lista vázia!")
            return

        aux = self._inicio
        for i in range(self._numItens - 1):
            print(f"Nome: {self._lista[aux].item.nome}, CPF: {self._lista[aux].item.cpf}", end=" | ")
            aux = self._lista[aux]._prox

        print(f"Nome: {self._lista[aux].item.nome}, CPF: {self._lista[aux].item.cpf}", end="\n")
        return

    def reordenaCpf(self) -> None:
        if self.vazia():
            return

        inicioOrdenado = _TERRA
        atual = self._inicio

        for i in range(self._numItens):
            proximo = self._lista[atual]._prox

            if inicioOrdenado == _TERRA or self._lista[atual].item.cpf <= self._lista[inicioOrdenado].item.cpf:
                self._lista[atual]._prox = inicioOrdenado
                inicioOrdenado = atual
            else:
                anterior = inicioOrdenado

                while self._lista[anterior]._prox != _TERRA and self._lista[self._lista[anterior]._prox].item.cpf <= self._lista[atual].item.cpf:
                    anterior = self._lista[anterior]._prox

                self._lista[atual]._prox = self._lista[anterior]._prox
                self._lista[anterior]._prox = atual

            atual = proximo

        self._inicio = inicioOrdenado

    def esvazia(self) -> None:
        self._inicio: int = _TERRA
        self._lista: list[TipoNo] = [TipoNo() for i in range(self._tamMax)]
        self._livres: int = 0 if self._tamMax > 0 else _TERRA
        self._numItens: int = 0
        self.item: TipoItem | None = None
        
        for i in range(self._tamMax - 1):
            self._lista[i]._prox = i + 1
        
        if self._tamMax > 0:
            self._lista[self._tamMax - 1]._prox = _TERRA