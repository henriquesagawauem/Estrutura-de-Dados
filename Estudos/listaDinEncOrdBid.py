from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoNo:
    nome: str = ""
    cpf: str = ""
    _prox: "TipoNo | None" = None
    _ant: "TipoNo | None" = None

class ListaDinEncOrdBid:
    def __init__(self):
        self._inicio: TipoNo = None
        self._fim: TipoNo = None
        self._numItens: int = 0

    def vazia(self) -> bool:
        return self._numItens == 0

    def _buscaAnterior(self, nome: str) -> TipoNo:
        anterior = None
        atual = self._inicio

        while atual != None and atual.nome < nome:
            anterior = atual
            atual = atual._prox

        return anterior

    def inserir(self, nome: str, cpf: str) -> bool:
        anterior = self._buscaAnterior(nome)

        if anterior == None:
            atual = self._inicio
        else:
            atual = anterior._prox

        if atual != None and atual.nome <= nome:
            return False

        novoNo: TipoNo = TipoNo(nome, cpf)

        if self.vazia():
            self._inicio = novoNo
            self._fim = novoNo

        elif anterior == None:
            novoNo._prox = self._inicio
            self._inicio._ant = novoNo
            self._inicio = novoNo

        elif atual == None:
            novoNo._ant = self._fim
            self._fim._prox = novoNo
            self._fim = novoNo
        else:
            novoNo._ant = anterior
            novoNo._prox = atual

            anterior._prox = novoNo
            atual._ant = novoNo
        self._numItens += 1

        return True

    def remover(self, nome: str) -> bool:
        if self.vazia():
            return False

        anterior = self._buscaAnterior(nome)

        if anterior == None:
            atual = self._inicio
        else:
            atual = anterior._prox

        if atual == None or atual.nome != nome:
            return False

        if anterior == None:
            self._inicio = atual._prox
        else:
            anterior._prox = atual._prox

        if atual._prox == None:
            self._fim = atual._ant
        else:
            atual._prox._ant = atual._ant

        self._numItens -= 1
        return True

    def mostra(self) -> bool:
        if self.vazia():
            print("Lista vázia")
            return

        aux = self._inicio
        for i in range(self._numItens):
            print(f"Nome: {aux.nome} | Anterior = {aux._ant.nome if aux._ant != None else None} | Proximo: {aux._prox.nome if aux._prox != None else None}")
            aux = aux._prox

        print()
        return

    def reorganizaCpf(self) -> None:
        inicioOrdenado = None
        fimOrdenado = None
        atual = self._inicio

        while atual != None:
            proximo = atual._prox

            if inicioOrdenado == None or atual.cpf <= inicioOrdenado.cpf:
                atual._prox = inicioOrdenado
                atual._ant = None
                if inicioOrdenado != None:
                    inicioOrdenado._ant = atual
                inicioOrdenado = atual
            else:
                anterior = inicioOrdenado

                while anterior._prox != None and anterior._prox.cpf <= atual.cpf:
                    anterior = anterior._prox

                atual._prox = anterior._prox
                atual._ant = anterior

                if anterior._prox != None:
                    anterior._prox._ant = atual

                anterior._prox = atual

            atual = proximo

        self._inicio = inicioOrdenado
        self._fim = fimOrdenado

                
                    


l = ListaDinEncOrdBid()

l.inserir("Henrique", "0")
l.inserir("Gabriel", "1")
l.inserir("Antonio", "2")
l.inserir("Vasco", "3")
l.inserir("Flavio", "4")

l.mostra()

l.reorganizaCpf()
l.mostra()

# l.remover("Henrique")
# l.remover("Vasco")
# l.remover("Antonio")
# l.mostra()