"""
Módulo que implementa um TAD de Fila Dinamica Encadeada. Nesse caso, a fila é
implementada como uma estrutura de nó conectados, na qual cada nó contém o
item do dado enfileirado e a referencia do próximo nó. A cada inserção um novo
nó é inserido (enfileiramento) e a cada remoção um nó é removido (desenfileiramento).

Em uma fila podemos enfileirar e desenfileira itens de dados, usando métodos
específicos definidos para essa finalidade. Não podemos manipular os dados
se não for por meio desses métodos. Sempre que precisar enfileirar um novo
item na fila, devemos inseri-lo no final da fila (após todos os demais que já
estão na fila) e sempre precisar desenfileirar um item, devemos remover o item que
está no início da fila.

Portanto, uma fila funciona segundo o modelo FIFO (First In First Out), ou seja,
o primeiro a entrar é o primeiro a sair. Ou LILO. 

Podemos também consultar o item que está no início da fila, que será o próximo
a sair. A consulta do item que está por último também pode ser implementada,
mas não é uma operação padrão, pois, em tese, para chegar a vez do último item,
todos os anteriores deveriam ser antes removidos. Não podemos acessar os itens
no meio da fila, intermediários.

A fila dinâmica é controlada por duas variáveis de referência: primeiro e último.
A variável primeiro aponta/referencia para o primeiro nó/item da fila, aquele que
será desenfileirado. A variável último aponta para o último nó/item da fila,
aquele que será o último a ser desenfileirado. As novas inserções são feitas atrás
do último, se tornando os novo últimos nós/itens. No início, ambas as variáveis
primeiro e último apontam/referenciam None, pois a fila está vazia. Na fila encadeada,
cada nó aponta para o próximo, no sentido do ultimo ao primeiro, formando um
encadeameento unidirecional.

Como a estrutura é estática, ela comporta uma quantidade máxima de itens.
"""
from __future__ import annotations #resolve referencia futura, como na classe _tipoNo
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class tipoItem:
    """
    Define o tipo do item da fila, ou seja, o tipo do dado que será enfileirado
    ou desenfileirado. No caso aqui, apenas um valor inteiro, mas poderia ser um
    conjunto de valores, tipo: nome, idade, CPF etc...
    """
    valor: str | int | float | None = None

"""
O _tipoNo define o tipo da unidade básica de alocação, chamada de Nó, o qual é
inserido no final da fila a cada novo enfileiramento. Ele comporta dois campos/
atrtibutos: o item de dado em si e um campo de referencia para o próximo Nó.
Observe que o atributo _prox é do mesmo tipo que a própria classe que ele
pertence, sendo necessário colocar o nome da classe entre aspas para defini-lo
desta forma. Exigencia do Python.
"""

@dataclass
class _tipoNo:
    item: tipoItem | None = None
    _prox: _tipoNo | None = None #para encadear/ligar os elementos dinamicamente



class filaEstDin(): #nesse caso, Fila Dinâmica Encadeada
    """
    Construtor da fila. Incializa os atributos que gerenciam o TAD.

    self._maxTam:      tamanho do vetor alocado; não usado efetivamente;
                       serve apenas para compatilbilzar a classe
    self._primeiro:    marcador do primeiro elemento (início da fila)
    self._ultimo:      marcador do último elemento (final da fila)
    self._numItens:    controla a quantidade de itens na fila
    self.item:          armazena uma cópia do item do ultimo desenfileiramento
    """

    def __init__(self, maxTam: int | None = None):
        self._primeiro: _tipoNo | None = None
        self._ultimo:   _tipoNo | None = None
        self._numItens: int            = 0
        self.item:      tipoItem | None = None
    
    def vazia(self) -> bool:
        return self._primeiro==None #ou self._numItens==0

    """
    Na estrutura dinamica não existe a possibilidade de fila cheia,
    mas esta função está sendo considerada para compatilbilizar com
    a estrutura estática. Isso permite executar as aplicações feitas
    para a estrutura estática.
    """
    def cheia(self) -> bool:
        return False

    def enfileira(self, item: tipoItem) -> bool:
        """
        Insere um novo elemento no final da fila, após o último. Esse novo elemento
        passa a ser o novo último. Altera o marcador de final de fila. Se for a
        primeira inserção, altera também o marcador do início da fila. Aumenta a
        quantidade de elementos. Retorna o suscesso da operação. 
        """
        if self.cheia():
            return False
        else:
            novoNo:_tipoNo = _tipoNo()
            novoNo.item = deepcopy(item)
            #novoNo._prox já está apontado pra None
            if self.vazia():
                self._primeiro=novoNo
                self._ultimo=novoNo    
            else:
                self._ultimo._prox=novoNo
                self._ultimo=novoNo
            self._numItens=self._numItens+1
            return True

    def desenfileira(self) -> bool:
        """
        Caso a estrutura não esteja vazia, remove o elemento que está no início,
        da fila, fazendo com que o elemento depois deste seja o novo início. Altera
        o marcador de início de fila. Se for o último da fila, altera o marcador
        do último também. Diminui a quantidade de elementos. Retorna uma cópia
        do elemento removido em self.item. Retorna o suscesso da operação.
        """
        if self.vazia():
            self.item=None
            return False
        else:
            aux:_tipoNo = self._primeiro 
            self._primeiro = self._primeiro._prox
            self.item=deepcopy(aux.item)
            aux._prox = None #não obrigatório, mas ajuda o coletor de lixo
            self._numItens=self._numItens-1
            if self.vazia():
                self._ultimo=None
            return True
    
    def itemPrimeiro(self) -> tipoItem:
        """
        Caso a estrutura não esteja vazia, retorna uma cópia do elemento que
        está na primeira posição, sem precisar removê-lo. O marcador de início
        continua com o mesmo valor. Não altera a quantidade de elementos.
        """
        if self.vazia():
            return None
        else:
            return deepcopy(self._primeiro.item)
        
    def mostra(self) -> None:
        """
        Mostra os elementos enfileirados, do primeiro até o último. Este método não
        faz parte do TAD em si, mas existe aqui apenas para fins didáticos.
        """
        if self.vazia():
            print("\nSituação da Fila: Vazia!")
        else:
            print("\nSituação da Fila: ",end="")
            pos=self._primeiro
            for i in range(self._numItens-1):
                print(pos.item.valor,", ", sep="",end="")
                pos=pos._prox
            if (self._numItens>0) and pos!= None:
                print(pos.item.valor)
            print("")

    def esvazia(self) -> None:
        """
        Reinicia os controles da fila para o estado inicial
        """
        self._primeiro: _tipoNo   = None
        self._ultimo: _tipoNo     = None
        self._numItens            = 0
        self.item                  = None

        

