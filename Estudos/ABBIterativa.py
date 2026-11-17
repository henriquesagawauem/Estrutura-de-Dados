from copy import deepcopy
from dataclasses import dataclass

from pilhaDinamica import PilhaDinamica
from filaDinamica import FilaDinamica


@dataclass
class TipoItem:
    nome: str | None = None
    cpf: str | None = None
    idade: int | None = None

@dataclass
class TipoNo:
    item: TipoItem | None = None
    _esq: "TipoNo | None" = None
    _dir: "TipoNo | None" = None

ARVOREVAZIA = 1
ARVORECHEIA = 2
ITEMEXISTENTE = 3
ITEMINEXISTENTE = 4
ITEMINSERIDO = 5
ITEMREMOVIDO = 6
ITEMATUALIZADO = 7


class ArvoreBinariaDeBuscaIterativa:
    def __init__(self):
        self._raiz: TipoNo | None = None
        self._numItens: int = 0
        self.item: TipoItem | None = None
        self._opStatus: int = ARVOREVAZIA

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return False

    def opStatus(self) -> int:
        return self._opStatus

    def totalItens(self) -> int:
        return self._numItens

    def insere(self, item: TipoItem) -> bool:
        if self.cheia():
            self._opStatus = ARVORECHEIA
            return False

        if self.vazia():
            self._raiz = TipoNo(item=deepcopy(item))
            self._opStatus = ITEMINSERIDO
            self._numItens += 1
            return True

        anterior: TipoNo = None
        atual: TipoNo = self._raiz

        while atual != None:
            if item.nome > atual.item.nome:
                anterior = atual
                atual = atual._dir
            elif item.nome < atual.item.nome:
                anterior = atual
                atual = atual._esq
            else:
                self._opStatus = ITEMEXISTENTE
                return False 

        novoNo: TipoNo = TipoNo(item=deepcopy(item))

        if item.nome < anterior.item.nome:
            anterior._esq = novoNo
        else:
            anterior._dir = novoNo

        self._opStatus = ITEMINSERIDO
        self._numItens += 1
        return True

    def _maiorDosMenores(self, no: TipoNo) -> TipoItem:
        anterior = None
        atual = no._esq

        while atual._dir != None:
            anterior = atual
            atual = atual._dir

        if anterior == None:
            no._esq = atual._esq
        else:
            anterior._dir = atual._esq

        return deepcopy(atual.item)

    def _menorDosMaiores(self, no: TipoNo) -> TipoItem:
        anterior = None
        atual = no._dir

        while atual._esq != None:
            anterior = atual
            atual = atual._esq

        if anterior == None:
            no._dir = atual._dir
        else:
            anterior._esq = atual._dir

        return deepcopy(atual.item)

    def remover(self, nome: str) -> bool:
        if self.vazia():
            self._opStatus = ARVOREVAZIA
            self.item = None
            return False

        anterior = None
        atual = self._raiz

        while atual != None and atual.item.nome != nome:
            if nome > atual.item.nome:
                anterior = atual
                atual = atual._dir
            else:
                anterior = atual
                atual = atual._esq

        if atual == None:
            self._opStatus = ITEMINEXISTENTE
            self.item = None
            return False

        self.item = deepcopy(atual.item)

        if anterior == None:
            if atual._esq == None:
                self._raiz = atual._dir
            elif atual._dir == None:
                self._raiz = atual._esq
            else:
                atual.item = self._maiorDosMenores(atual)
        else:
            if nome > anterior.item.nome:
                if atual._esq == None:
                    anterior._dir = atual._dir
                elif atual._dir == None:
                    anterior._dir = atual._esq
                else:
                    atual.item = self._maiorDosMenores(atual)
            else:
                if atual._esq == None:
                    anterior._esq = atual._dir
                elif atual._dir == None:
                    anterior._esq = atual._esq
                else:
                    atual.item = self._maiorDosMenores(atual)

        self._opStatus = ITEMREMOVIDO
        self._numItens -= 1
        return True


    def mostraEmOrdem(self) -> None:
        if self.vazia():
            print("Árvore vázia.")
            return

        pilhaAux = PilhaDinamica()
        aux = self._raiz

        while not pilhaAux.vazia() or aux != None:
            if aux == None:
                item = pilhaAux.topo()
                pilhaAux.desempilha()

                aux = item

                print(aux.item.nome, end=" ")

                aux = aux._dir
            else:
                pilhaAux.empilha(aux)
                aux = aux._esq

        print()

    def mostraPreOrdem(self) -> None:
        if self.vazia():
            print("Árvore vázia.")
            return

        pilhaAux = PilhaDinamica()
        aux = self._raiz

        while not pilhaAux.vazia() or aux != None:
            if aux == None:
                item = pilhaAux.topo()
                pilhaAux.desempilha()

                aux = item

                aux = aux._dir
            else:
                print(aux.item.nome, end=" ")
                pilhaAux.empilha(aux)
                aux = aux._esq

        print()

    def mostraPosOrdem(self) -> None:
        if self.vazia():
            print("Árvore vázia")
            return

        pilha1 = PilhaDinamica()
        pilha2 = PilhaDinamica()

        pilha1.empilha(self._raiz)

        while not pilha1.vazia():
            item = pilha1.topo()
            pilha1.desempilha()

            pilha2.empilha(item)

            if item._esq != None:
                pilha1.empilha(item._esq)

            if item._dir != None:
                pilha1.empilha(item._dir)

        while not pilha2.vazia():
            item = pilha2.topo()
            pilha2.desempilha()

            print(item.item.nome, end=" ")

        print()

    def mostraEmLargura(self) -> None:
        if self.vazia():
            print("Árvore vázia.")
            return

        filaAux = FilaDinamica()

        filaAux.enfileira(self._raiz)

        while not filaAux.vazia():
            item = filaAux.primeiro()
            filaAux.desenfileira()

            print(item.item.nome, end=" ")

            if item._esq != None:
                filaAux.enfileira(item._esq)

            if item._dir != None:
                filaAux.enfileira(item._dir)

        print()

    def consulta(self, nome: str) -> TipoItem | None:
        if self.vazia():
            self._opStatus = ARVOREVAZIA
            return None

        anterior = None
        atual = self._raiz

        while atual != None and atual.item.nome != nome:
            if nome > atual.item.nome:
                anterior = atual
                atual = atual._dir
            elif nome < atual.item.nome:
                anterior = atual
                atual = atual._esq

        if atual == None or atual.item.nome != nome:
            self._opStatus = ITEMINEXISTENTE
            return None

        return deepcopy(atual.item)

    def atualiza(self, item: TipoItem) -> bool:
        if self.vazia():
            self._opStatus = ARVOREVAZIA
            return False

        nome = item.nome

        anterior = None
        atual = self._raiz
    
        while atual != None and atual.item.nome != nome:
            if nome > atual.item.nome:
                anterior = atual
                atual = atual._dir
            elif nome < atual.item.nome:
                anterior = atual
                atual = atual._esq
    
        if atual == None or atual.item.nome != nome:
            self._opStatus = ITEMINEXISTENTE
            return False

        atual.item.idade = deepcopy(item.idade)
        atual.item.cpf = deepcopy(item.cpf)

        self._opStatus = ITEMATUALIZADO

        return True

arvore = ArvoreBinariaDeBuscaIterativa()

arvore.insere(TipoItem("Henrique"))
arvore.insere(TipoItem("Fernando"))
arvore.insere(TipoItem("Sergio"))
arvore.insere(TipoItem("Breno"))
arvore.insere(TipoItem("Gustavo"))
arvore.insere(TipoItem("Antonio"))
arvore.insere(TipoItem("Carlos"))
arvore.insere(TipoItem("Matheus"))
arvore.insere(TipoItem("Marcos"))
arvore.insere(TipoItem("Senna"))
arvore.insere(TipoItem("João"))

arvore.mostraEmOrdem()
print()
arvore.mostraPreOrdem()
print()
arvore.mostraPosOrdem()
print()
arvore.mostraEmLargura()
print()

print(arvore.consulta("Henrique"))
print(arvore.consulta("Marcos"))
print(arvore.consulta("Gustavo"))

print()

print(arvore.atualiza(TipoItem("Henrique", "111111", 11)))
print(arvore.atualiza(TipoItem("Marcos", "222222", 22)))
print(arvore.atualiza(TipoItem("Gustavo", "333333", 33)))

print()

print(arvore.consulta("Henrique"))
print(arvore.consulta("Marcos"))
print(arvore.consulta("Gustavo"))

print()

arvore.remover("Henrique")
arvore.remover("Marcos")
arvore.remover("Gustavo")
arvore.remover("Antonio")

arvore.mostraEmOrdem()
print()
arvore.mostraPreOrdem()
print()
arvore.mostraPosOrdem()
print()
arvore.mostraEmLargura()
print()