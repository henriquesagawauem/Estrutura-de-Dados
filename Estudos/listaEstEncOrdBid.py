from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoNo:
    nome: str = ""
    cpf: str = ""
    _prox: int = 0
    _ant: int = 0


_TERRA: int = -1


class ListaEstEncOrdBid:
    def __init__(self, tamMax: int):
        self._tamMax: int = tamMax
        self._inicio: int = _TERRA
        self._fim: int = _TERRA
        self._lista: list[TipoNo] = [TipoNo() for i in range(tamMax)]
        self._livres: int = 0 if tamMax > 0 else _TERRA
        self._numItens: int = 0

        for i in range(tamMax - 1):
            self._lista[i]._prox = i + 1
            self._lista[i]._ant = i - 1

        if tamMax > 0:
            self._lista[tamMax - 1]._prox = _TERRA
            self._lista[tamMax - 1]._ant = tamMax - 2

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._tamMax

    def _buscaAnterior(self, nome: str) -> int:
        anterior = _TERRA
        atual = self._inicio

        while atual != _TERRA and self._lista[atual].nome < nome:
            anterior = atual
            atual = self._lista[atual]._prox

        return anterior

    def inserir(self, nome: str, cpf: str) -> bool:
        if self.cheia():
            return False

        anterior = self._buscaAnterior(nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior]._prox

        if atual != _TERRA and self._lista[atual].nome <= nome:
            return False

        novaPosicao = self._livres
        self._livres = self._lista[novaPosicao]._prox

        self._lista[novaPosicao].nome = deepcopy(nome)
        self._lista[novaPosicao].cpf = deepcopy(cpf)

        self._lista[novaPosicao]._prox = atual
        self._lista[novaPosicao]._ant = anterior

        if anterior == _TERRA:
            self._inicio = novaPosicao
        else:
            self._lista[anterior]._prox = novaPosicao

        if atual == _TERRA:
            self._fim = novaPosicao
        else:
            self._lista[atual]._ant = novaPosicao

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

        if atual == _TERRA or self._lista[atual].nome != nome:
            return False

        if anterior == _TERRA:
            self._inicio = self._lista[atual]._prox
            self._lista[self._inicio]._ant = _TERRA
        else:
            self._lista[anterior]._prox = self._lista[atual]._prox
            self._lista[atual]._ant = anterior

        if self._fim == None:
            self._fim = self._lista[self._fim]._ant

        self._numItens -= 1

        return True

    def mostra(self) -> None:
        if self.vazia():
            print("Lista vázia")
            return

        aux = self._inicio

        for i in range(self._numItens):
            print(
                f"Nome: {self._lista[aux].nome} | Anterior = {self._lista[self._lista[aux]._ant].nome if self._lista[aux]._ant != _TERRA else _TERRA} | Proximo = {self._lista[self._lista[aux]._prox].nome if self._lista[aux]._prox != _TERRA else _TERRA} -> CPF = {self._lista[aux].cpf}"
            )
            aux = self._lista[aux]._prox

        print()
        return

    def reorganizaCpf(self) -> None:
        inicioOrdenado = _TERRA
        fimOrdenado = _TERRA
        atual = self._inicio

        for i in range(self._numItens):
            proximo = self._lista[atual]._prox

            if (
                inicioOrdenado == _TERRA
                or self._lista[atual].cpf <= self._lista[inicioOrdenado].cpf
            ):
                self._lista[atual]._prox = inicioOrdenado
                self._lista[atual]._ant = _TERRA

                if inicioOrdenado != _TERRA:
                    self._lista[inicioOrdenado]._ant = atual

                inicioOrdenado = atual

            else:
                anterior = inicioOrdenado

                while (
                    self._lista[anterior]._prox != _TERRA
                    and self._lista[self._lista[anterior]._prox].cpf
                    <= self._lista[atual].cpf
                ):
                    anterior = self._lista[anterior]._prox

                self._lista[atual]._prox = self._lista[anterior]._prox
                self._lista[atual]._ant = anterior

                if self._lista[anterior]._prox != _TERRA:
                    self._lista[self._lista[anterior]._prox]._ant = atual
                else:
                    fimOrdenado = atual

                self._lista[anterior]._prox = atual
            atual = proximo

        self._inicio = inicioOrdenado
        self._fim = fimOrdenado


l = ListaEstEncOrdBid(5)

l.inserir("Henrique", "0")
l.inserir("Gabriel", "1")
l.inserir("Antonio", "2")
l.inserir("Vasco", "3")
l.inserir("Flavio", "4")

l.mostra()

l.reorganizaCpf()
l.mostra()