from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    nome: str | None = None
    cpf: str | None = None
    idade: int | None = None

@dataclass
class TipoNo:
    item: TipoItem | None = None
    _prox: "TipoNo | None" = None

TABELAVAZIA = 1
ITEMEXISTENTE = 2
ITEMINEXISTENTE = 3
ITEMINSERIDO = 4
ITEMREMOVIDO = 5
ITEMATUALIZADO = 6


class TabelaHash:
    def __init__(self, tamMax: int):
        self._tamMax: int = tamMax
        self._tabela: list[TipoNo | None] = [None for i in range(tamMax)]
        self._numItens: int = 0
        self._opStatus: int = TABELAVAZIA

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return False

    def opStatus(self) -> int:
        return self._opStatus

    def totalItens(self) -> int:
        return self._numItens

    def _hash(self, chave: str) -> int:
        valor: int = 0

        for caractere in chave:
            valor = (valor * 31 + ord(caractere)) % self._tamMax

        return valor

    def insere(self, item: TipoItem) -> bool:
        posicao: int = self._hash(item.cpf)
        atual: TipoNo | None = self._tabela[posicao]

        while atual != None:
            if atual.item.cpf == item.cpf:
                self._opStatus = ITEMEXISTENTE
                return False
            atual = atual._prox

        novoNo: TipoNo = TipoNo(item=deepcopy(item))
        novoNo._prox = self._tabela[posicao]
        self._tabela[posicao] = novoNo

        self._numItens += 1
        self._opStatus = ITEMINSERIDO
        return True

    def remove(self, cpf: str) -> bool:
        if self.vazia():
            self._opStatus = TABELAVAZIA
            return False

        posicao: int = self._hash(cpf)
        anterior: TipoNo | None = None
        atual: TipoNo | None = self._tabela[posicao]

        while atual != None and atual.item.cpf != cpf:
            anterior = atual
            atual = atual._prox

        if atual == None:
            self._opStatus = ITEMINEXISTENTE
            return False

        if anterior == None:
            self._tabela[posicao] = atual._prox
        else:
            anterior._prox = atual._prox

        self._numItens -= 1
        self._opStatus = ITEMREMOVIDO
        return True

    def consulta(self, cpf: str) -> TipoItem | None:
        if self.vazia():
            self._opStatus = TABELAVAZIA
            return None

        posicao: int = self._hash(cpf)
        atual: TipoNo | None = self._tabela[posicao]

        while atual != None and atual.item.cpf != cpf:
            atual = atual._prox

        if atual == None:
            self._opStatus = ITEMINEXISTENTE
            return None

        self._opStatus = ITEMEXISTENTE
        return deepcopy(atual.item)

    def atualiza(self, item: TipoItem) -> bool:
        if self.vazia():
            self._opStatus = TABELAVAZIA
            return False

        posicao: int = self._hash(item.cpf)
        atual: TipoNo | None = self._tabela[posicao]

        while atual != None and atual.item.cpf != item.cpf:
            atual = atual._prox

        if atual == None:
            self._opStatus = ITEMINEXISTENTE
            return False

        atual.item = deepcopy(item)
        self._opStatus = ITEMATUALIZADO
        return True

    def mostra(self) -> None:
        if self.vazia():
            print("Tabela vázia!")
            return

        for i in range(self._tamMax):
            print(f"[{i}] ", end="")
            aux = self._tabela[i]

            if aux == None:
                print("vazio")
                continue

            while aux._prox != None:
                print(f"{aux.item.cpf} ({aux.item.nome})", end=" -> ")
                aux = aux._prox

            print(f"{aux.item.cpf} ({aux.item.nome})")

        return

    def esvazia(self) -> None:
        self._tabela = [None for i in range(self._tamMax)]
        self._numItens = 0
        self._opStatus = TABELAVAZIA