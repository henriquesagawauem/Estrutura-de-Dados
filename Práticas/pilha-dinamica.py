from dataclasses import dataclass
from typing import Optional

@dataclass
class TipoItem:
    valor: None | int | float | str = None

@dataclass
class _TipoNo:
    item: TipoItem
    _prox: Optional["_TipoNo"] = None

class Pilha:
    def __init__(self) -> None:
        self._topo: Optional[_TipoNo] = None
        self._numsItens: int = 0

    def vazia(self) -> bool:
        return self._numsItens == 0

    def cheia(self) -> bool:
        return False

    def empilha(self, item: TipoItem) -> bool:
        novo_no = _TipoNo(item=item, _prox=self._topo)
        self._topo = novo_no
        self._numsItens += 1
        return True

    def desempilha(self) -> Optional[TipoItem]:
        if self.vazia() or self._topo is None:
            return None

        item_removido = self._topo.item
        self._topo = self._topo._prox
        self._numsItens -= 1
        return item_removido

    def topo(self) -> Optional[TipoItem]:
        if self.vazia() or self._topo is None:
            return None
        return self._topo.item

    def mostra(self) -> None:
        if self.vazia():
            print("Pilha vazia :(")
            return

        pos = self._topo
        print("Topo -> ", end="")
        while pos is not None:
            print(f"[{pos.item.valor}]", end=" -> ")
            pos = pos._prox
        print("Base")

    def esvazia(self) -> None:
        self._topo = None
        self._numsItens = 0



def testar_pilha():
    p = Pilha()

    print("--- 1. Pilha Recém-Criada ---")
    print(f"Está vazia? {p.vazia()}")
    print(f"Topo atual: {p.topo()}")
    p.mostra()

    print("\n--- 2. Inserindo Elementos (Empilha) ---")
    p.empilha(TipoItem("Elemento 1"))
    p.empilha(TipoItem(100))
    p.empilha(TipoItem(9.99))
    
    print(f"Está vazia? {p.vazia()}")              
    print(f"Topo atual (esperado 9.99): {p.topo().valor}") 
    p.mostra()

    print("\n--- 3. Removendo Elementos (Desempilha - LIFO) ---")
    item1 = p.desempilha()
    print(f"Removido 1: {item1.valor if item1 else None}") 
    
    item2 = p.desempilha()
    print(f"Removido 2: {item2.valor if item2 else None}") 
    
    print("\nEstado da pilha após duas remoções:")
    p.mostra()

    print("\n--- 4. Esvaziando a Pilha ---")
    p.esvazia()
    print(f"Está vazia após esvaziar()? {p.vazia()}") 
    print(f"Topo atual: {p.topo()}")                   

    print("\n--- 5. Teste de Borda (Desempilhar pilha vazia) ---")
    item_vazio = p.desempilha()
    print(f"Resultado ao desempilhar pilha vazia: {item_vazio}") 


if __name__ == "__main__":
    testar_pilha()