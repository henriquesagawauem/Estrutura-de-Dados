from dataclasses import dataclass
from copy import deepcopy

@dataclass
class TipoItem:
    nome: str | None = None
    cpf: str | None = None
    idade: int | None = None

@dataclass
class TipoNo:
    item: TipoItem | None = None
    _esq: 'TipoNo | None' = None
    _dir: 'TipoNo | None' = None
    _bal: int = 0

ARVORECHEIA = 1
ARVOREVAZIA = 2
ITEMEXISTENTE = 3
ITEMINEXISTENTE = 4
ITEMINSERIDO = 5
ITEMREMOVIDO = 6

class ArvoreAVLRecursiva:
    def __init__(self):
        self._raiz: TipoNo | None = None
        self._numItens: int = 0
        self.item: TipoItem | None = None
        self.opStatus: int = ARVOREVAZIA

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return False

    def totalItens(self) -> int:
        return self._numItens

    def _altura(self, no: TipoNo) -> int:
        if no == None:
            return 0

        alturaEsq = self._altura(no._esq)
        alturaDir = self._altura(no._dir)

        if alturaEsq > alturaDir:
            return alturaEsq + 1

        return alturaDir + 1

    def _atualizaBal(self, no: TipoNo) -> None:
        if no == None:
            return

        no._bal = self._altura(no._dir) - self._altura(no._esq)

    def _rotacaoDireita(self, raiz: TipoNo):
        novaRaiz = raiz._esq

        raiz._esq = novaRaiz._dir
        novaRaiz._dir = raiz

        self._atualizaBal(raiz)
        self._atualizaBal(novaRaiz)

        return novaRaiz

    def _rotacaoEsquerda(self, raiz: TipoNo) -> TipoNo:
        novaRaiz = raiz._dir

        raiz._dir = novaRaiz._esq
        novaRaiz._esq = raiz

        self._atualizaBal(raiz)
        self._atualizaBal(novaRaiz)

        return novaRaiz

    def _balancear(self, raiz: TipoNo):
        if raiz == None:
            return raiz

        self._atualizaBal(raiz)

        if raiz._bal > 1:
            self._atualizaBal(raiz._dir)

            if raiz._dir._bal < 0:
                raiz._dir = self._rotacaoDireita(raiz._dir)

            return self._rotacaoEsquerda(raiz)

        if raiz._bal < -1:
            self._atualizaBal(raiz._esq)

            if raiz._esq._bal > 0:
                raiz._esq = self._rotacaoEsquerda(raiz._esq)

            return self._rotacaoDireita(raiz)

        return raiz

    def _insereAVL(self, raiz: TipoNo, item: TipoItem):
        if raiz == None:
            novo = TipoNo()
            novo.item = deepcopy(item)

            self._numItens += 1
            self.opStatus = ITEMINSERIDO

            return novo

        if item.nome < raiz.item.nome:
            raiz._esq = self._insereAVL(raiz._esq, item)
        elif item.nome > raiz.item.nome:
            raiz._dir = self._insereAVL(raiz._dir, item)
        else:
            return raiz

        if self.opStatus == ITEMINSERIDO:
            raiz = self._balancear(raiz)

        return raiz

    def insereAVL(self, item: TipoItem) -> bool:
        if self.cheia():
            self.opStatus = ARVORECHEIA
            return False

        self.opStatus = ITEMEXISTENTE

        self._raiz = self._insereAVL(self._raiz, item)

        return self.opStatus == ITEMINSERIDO

    def _mostraEmOrdemAux(self, no: TipoNo) -> None:
        if no != None:
            self._mostraEmOrdemAux(no._esq)
            print(no.item.nome, end=" ")
            self._mostraEmOrdemAux(no._dir)

    def mostraEmOrdem(self) -> None:
        if self.vazia():
            self.opStatus = ARVOREVAZIA
            print("Árvore vázia")
            return

        print("Em-ordem: ", end='')
        self._mostraEmOrdemAux(self._raiz)

        print()
        return

    def _mostraPreOrdemAux(self, no: TipoNo) -> None:
        if no != None:
            print(no.item.nome, end=" ")
            self._mostraPreOrdemAux(no._esq)
            self._mostraPreOrdemAux(no._dir)

    def mostraPreOrdem(self) -> None:
        if self.vazia():
            print("Árvore vázia.")
            return

        print("Pré-ordem: ", end="")
        self._mostraPreOrdemAux(self._raiz)
        print()

        return

    def _mostraPosOrdemAux(self, no: TipoNo) -> None:
        if no != None:
            self._mostraPosOrdemAux(no._esq)
            self._mostraPosOrdemAux(no._dir)
            print(no.item.nome, end=" ")

    def mostraPosOrdem(self) -> None:
        if self.vazia():
            print("Árvore vázia.")
            return

        print("Pós-ordem: ", end=" ")
        self._mostraPosOrdemAux(self._raiz)
        print()
        return

    def _maiorDosMenores(self, raiz: TipoNo) -> TipoNo:

        while raiz._dir != None:
            raiz = raiz._dir

        return raiz

    def _removeAVL(self, raiz: TipoNo | None, nome: str, guardar: bool) -> TipoNo | None:
        if raiz == None:
            return None

        if nome < raiz.item.nome:
            raiz._esq = self._removeAVL(raiz._esq, nome, guardar)
        elif nome > raiz.item.nome:
            raiz._dir = self._removeAVL(raiz._dir, nome, guardar)
        else:
            if guardar:
                self.item = deepcopy(raiz.item)
                self.opStatus = ITEMREMOVIDO
                self._numItens -= 1

            if raiz._esq == None:
                return raiz._dir

            if raiz._dir == None:
                return raiz._esq

            predecessor = self._maiorDosMenores(raiz._esq)

            raiz.item = deepcopy(predecessor.item)

            raiz._esq = self._removeAVL(raiz._esq, predecessor.item.nome, False)

        raiz = self._balancear(raiz)

        return raiz

    def removeAVL(self, nome: str) -> bool:
        if self.vazia():
            self.opStatus = ARVOREVAZIA
            return False

        self.opStatus = ITEMEXISTENTE
        self.item = None

        self._raiz = self._removeAVL(self._raiz, nome, True)

        return self.item

    def _mostraNível(self, raiz: TipoNo, nivel: int) -> None:
        if raiz == None:
            return

        if nivel == 1:
            print(raiz.item.nome, end=" ")
        else:
            self._mostraNível(raiz._esq, nivel - 1)
            self._mostraNível(raiz._dir, nivel - 1)

    def mostraEmLargura(self) -> None:
        if self.vazia():
            print("Árvore vázia.")
            return

        altura = self._altura(self._raiz)

        print("Em-largura: ", end="")

        for nivel in range(1, altura + 1):
            self._mostraNível(self._raiz, nivel)

        print()
        return

    def _consultaAux(self, raiz: TipoNo, nome: str) -> TipoItem | None:
        if raiz == None:
            return None

        if nome < raiz.item.nome:
            return self._consultaAux(raiz._esq, nome)
        elif nome > raiz.item.nome:
            return self._consultaAux(raiz._dir, nome)
        else:
            return deepcopy(raiz.item)

    def consulta(self, nome: str) -> TipoItem | None:
        if self.vazia():
            self.opStatus = ARVOREVAZIA
            return None

        self.opStatus = ITEMINEXISTENTE

        item = self._consultaAux(self._raiz, nome)

        if item != None:
            self.opStatus = ITEMEXISTENTE

        return item

    def reinicia(self) -> None:
        self._raiz = None
        self._numItens = 0
        self.item = None
        self.opStatus = ARVOREVAZIA




if __name__ == "__main__":

    print("\nTestador de TAD Arvore Binaria de Busca AVL Recursiva\n")
    arv=ArvoreAVLRecursiva()
    arv.mostraEmOrdem()
    
    item=TipoItem("RON","178.763.238-55",58)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("ANA","145.583.148-77",50)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("BEN","049.343.648-23",25)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("BER","456.432.863-90",35)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("XER","451.761.098-32",30)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("AAR","023.453.984-89",48)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("BEA","189.982.345-10",38)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()
    
    item=TipoItem("CAR","786.340.671-39",22)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("SER","340.456.671-93",29)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("PAU","544.999.761-00",32)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("DAN","111.222.347-78",42)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("CAI","339.983.456-13",19)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("XIN","538.720.912-44",31)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("BAR","123.432.455-66",80)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("BEP","338.320.312-34",12)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=TipoItem("XES","518.721.911-41",1)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    
    arv.mostraEmOrdem()
    arv.mostraPreOrdem()
    arv.mostraPosOrdem()
    arv.mostraEmLargura()
    

    print("\nRemovendo: ", end="")
    if arv.removeAVL("SER"):
        print(arv.item.nome)
        
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("BER")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("RON")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("ANA")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("PAU")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("BEN")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("CAR")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("CAI")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("DAN")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("AAR")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("XER")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("BEA")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("BEP")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("XIN")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("BAR")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: TipoItem=arv.removeAVL("XES")
    print(item.nome)
    arv.mostraEmOrdem()