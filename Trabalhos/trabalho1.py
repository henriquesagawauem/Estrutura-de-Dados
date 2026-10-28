# Henrique Tutomu Sagawa - RA152725

from copy import deepcopy
from dataclasses import dataclass


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


ACOUGUE = 1
PADARIA = 2
FRIOSELATICINIOS = 3
HIGIENECORPORAL = 4
LIMPEZA = 5
HORTIFRUTI = 6
GRAOSFARINACEOSECAFE = 7
BEBIDAS = 8
UTENSILIOS = 9
DIVERSOS = 10


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
            while atual.prox is not None and atual.prox.item.nome <= item.nome:
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

    def relatorioEstoqueTotal(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio
        primeiro = True

        print("Relatório de produtos em estoque: ")
        while atual != None:
            if atual.item.quantidade_estoque > 0:
                if not primeiro:
                    print(", ", end="")
                print(atual.item.nome, end="")
                primeiro = False
            atual = atual.prox

        print()
        return

    def relatorioEstoqueTipo(self, tipo: int):
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        print(f"Relatório de produtos em estoque do tipo {tipo}: ")
        primeiro = True
        while atual != None:
            if atual.item.tipo == tipo and atual.item.quantidade_estoque > 0:
                if not primeiro:
                    print(", ", end="")
                print(atual.item.nome, end="")
                primeiro = False
            atual = atual.prox

        print()

        return

    def relatorioProdutosEsgotados(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio
        primeiro = True

        print("Relatório de produtos esgotados: ")
        while atual != None:
            if atual.item.quantidade_estoque == 0:
                if not primeiro:
                    print(", ", end="")
                print(atual.item.nome, end="")
                primeiro = False
            atual = atual.prox

        print()

        return

    def relatorioProdutosEstoqueBaixo(self, limite: int) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        print(f"Relatório de produtos com estoque abaixo de {limite}: ")
        primeiro = True
        while atual != None:
            if atual.item.quantidade_estoque < limite:
                if not primeiro:
                    print(", ", end="")
                print(atual.item.nome, end="")
                primeiro = False
            atual = atual.prox

        print()

        return

    def relatorioQuantidadeVendida(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        print("Relatório de quantidade vendida: ")
        primeiro = True
        while atual != None:
            if atual.item.quantidade_vendida > 0:
                if not primeiro:
                    print(", ", end="")
                print(f"{atual.item.nome} ({atual.item.quantidade_vendida})", end="")
                primeiro = False
            atual = atual.prox

        print()

        return

    def relatorioTotalBruto(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio
        total_bruto = 0.0

        while atual != None:
            total_bruto += atual.item.quantidade_vendida * atual.item.valor_venda
            atual = atual.prox

        print(f"Relatório de total bruto: R$ {total_bruto:.2f}")

    def relatorioTotalLiquido(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio
        total_liquido = 0.0

        while atual != None:
            total_liquido += atual.item.quantidade_vendida * (atual.item.valor_venda - atual.item.valor_custo)
            atual = atual.prox

        print(f"Relatório de total líquido: R$ {total_liquido:.2f}")

    def reajustePercentual(self, percentual: float) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        while atual != None:
            atual.item.valor_venda *= (1 + percentual / 100)
            atual = atual.prox

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

    def reiniciaVendas(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        while atual != None:
            atual.item.quantidade_vendida = 0
            atual = atual.prox
