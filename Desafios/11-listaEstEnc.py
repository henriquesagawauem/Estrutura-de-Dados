from copy import deepcopy
from dataclasses import dataclass

_TERRA = -1


@dataclass
class TipoItem:
    nome: str = ""
    idade: int = 0


@dataclass
class No:
    item: TipoItem | None = None
    proximo: int = _TERRA


class ListaEstaticaEncadeada:
    def __init__(self, tamMax: int):
        self._tamMax = tamMax
        self._inicio = _TERRA

        self._lista: list[No] = [No() for _ in range(tamMax)]

        self._livres = 0 if tamMax > 0 else _TERRA

        for i in range(tamMax - 1):
            self._lista[i].proximo = i + 1

        if tamMax > 0:
            self._lista[tamMax - 1].proximo = _TERRA

    def vazia(self) -> bool:
        return self._inicio == _TERRA

    def cheia(self) -> bool:
        return self._livres == _TERRA

    def buscaAnterior(self, nome: str) -> int:
        anterior = _TERRA
        atual = self._inicio

        while atual != _TERRA and self._lista[atual].item.nome < nome:
            anterior = atual
            atual = self._lista[atual].proximo

        return anterior

    def inserir(self, item: TipoItem) -> bool:

        if self.cheia():
            return False

        anterior = self.buscaAnterior(item.nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior].proximo

        if atual != _TERRA and self._lista[atual].item.nome == item.nome:
            return False

        novaPosicao = self._livres

        self._livres = self._lista[novaPosicao].proximo

        self._lista[novaPosicao].item = deepcopy(item)

        if anterior == _TERRA:
            self._lista[novaPosicao].proximo = self._inicio
            self._inicio = novaPosicao

        else:
            self._lista[novaPosicao].proximo = self._lista[anterior].proximo

            self._lista[anterior].proximo = novaPosicao

        return True

    def remover(self, nome: str) -> bool:
        if self.vazia():
            return False

        anterior = self.buscaAnterior(nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior].proximo

        if atual == _TERRA or self._lista[atual].item.nome != nome:
            return False

        if anterior == _TERRA:
            self._inicio = self._lista[atual].proximo
        else:
            self._lista[anterior].proximo = self._lista[atual].proximo

        self._lista[atual].item = None
        self._lista[atual].proximo = self._livres
        self._livres = atual

        return True

    def consultar(self, nome: str) -> TipoItem | None:
        anterior = self.buscaAnterior(nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior].proximo

        if atual != _TERRA and self._lista[atual].item.nome == nome:
            return deepcopy(self._lista[atual].item)

        return None

    def atualizar(self, nome: str, novoItem: TipoItem) -> bool:

        anterior = self.buscaAnterior(nome)

        if anterior == _TERRA:
            atual = self._inicio
        else:
            atual = self._lista[anterior].proximo

        if atual == _TERRA or self._lista[atual].item.nome != nome:
            return False

        if novoItem.nome == nome:
            self._lista[atual].item = deepcopy(novoItem)
            return True

        itemAntigo = deepcopy(self._lista[atual].item)

        self.remover(nome)

        if self.inserir(novoItem):
            return True

        self.inserir(itemAntigo)

        return False

    def mostrar(self):
        atual = self._inicio

        print("LISTA: ")

        while atual != _TERRA:
            no = self._lista[atual]

            print(f"[{atual}] {no.item.nome}, {no.item.idade} -> {no.proximo}")

            atual = no.proximo

    def mostrarVetor(self):
        print("\nVETOR:")

        for i in range(self._tamMax):

            print(
                f"{i}: "
                f"item={self._lista[i].item}, "
                f"proximo={self._lista[i].proximo}"
            )

        print(f"\n_inicio = {self._inicio}")
        print(f"_livres = {self._livres}")