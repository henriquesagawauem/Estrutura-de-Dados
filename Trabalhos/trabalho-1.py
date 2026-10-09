# Henrique Tutomu Sagawa - RA152725

from dataclasses import dataclass
from copy import deepcopy

@dataclass
class TipoItem:
    nome: str = ""
    tipo: str = ""
    quantidade_estoque: int = 0
    quantidade_vendida: int = 0
    valor_custo: float = 0.0
    valor_venda: float = 0.0

@dataclass
class No:
    item: TipoItem
    prox: "No | None" = None

class ListaDinamicaEncadeada:
    def __init__(self):
        self._inicio: No = None
        self._nItens: int = 0

    def vazia(self):
        return self._inicio is None

    def cheia(self):
        return False

    def insere(self, item: TipoItem) -> bool:
        novo = No(deepcopy(item))

        if self.vazia() or item.nome < self._inicio.item.nome:
            novo.prox = self._inicio
            self._inicio = novo

        else:
            atual = self._inicio
            while (atual.prox is not None and atual.prox.item.nome <= item.nome):
                atual = atual.prox

            novo.prox = atual.prox
            atual.prox = novo

        self._nItens += 1
        return True

    def remove(self, nome: str) -> bool:
        if self.vazia():
            return False

        anterior = None
        atual = self._inicio

        while atual is not None and atual.item.nome < nome:
            anterior = atual
            atual = atual.prox

        if atual is None or atual.item.nome != nome:
            return False

        if anterior is None:
            self._inicio = atual.prox
        else:
            anterior.prox = atual.prox

        self._nItens -= 1
        return True

    def buscar(self, nome: str) -> TipoItem | None:
        if self.vazia():
            return None

        atual = self._inicio

        while atual is not None and atual.item.nome != nome:
            atual = atual.prox

        if atual is not None:
            return atual.item

        return None

    def mostra(self) -> None:
        atual = self._inicio

        contador = 1

        while atual is not None:
            print(f"{contador} - {atual.item.nome}")
            atual = atual.prox
            contador += 1

    def atualiza(self, itemAtualizado: TipoItem) -> bool:
        item = self.buscar(itemAtualizado.nome)

        if item is None:
            return False

        item.tipo = itemAtualizado.tipo
        item.quantidade_estoque = itemAtualizado.quantidade_estoque
        item.quantidade_vendida = itemAtualizado.quantidade_vendida
        item.valor_custo = itemAtualizado.valor_custo
        item.valor_venda = itemAtualizado.valor_venda

        return True

    def reinicia(self) -> None:
        self._inicio = None
        self._nItens = 0