# Henrique Tutomu Sagawa - RA152725
#
# Sistema de controle de mercado (trabalho 2), tudo em um único arquivo.
# A mesma interface (testador/menu) roda com duas estruturas diferentes:
#   - Árvore Binária de Busca ITERATIVA
#   - Árvore AVL RECURSIVA


from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    """
    tipo para os itens do mercado
    """
    nome: str = ""
    tipo: int = 0
    quantidade_estoque: int = 0
    quantidade_vendida: int = 0
    valor_custo: float = 0.0
    valor_venda: float = 0.0
    total_bruto: float = 0.0
    total_liquido: float = 0.0



# Catalogo do mercado marcado por constantes
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


def mostrarTipo(tipo: int) -> str:
    """ Recebe o tipo do produto por meio de um inteiro e retorna a string associada a ele """
    if tipo == ACOUGUE:
        return "Açougue"
    elif tipo == PADARIA:
        return "Padaria"
    elif tipo == FRIOSELATICINIOS:
        return "Frios e Laticínios"
    elif tipo == HIGIENECORPORAL:
        return "Higiene e Corporal"
    elif tipo == LIMPEZA:
        return "Limpeza"
    elif tipo == HORTIFRUTI:
        return "Hortifruti"
    elif tipo == GRAOSFARINACEOSECAFE:
        return "Grãos, Farináceos e Café"
    elif tipo == BEBIDAS:
        return "Bebidas"
    elif tipo == UTENSILIOS:
        return "Utensílios"
    elif tipo == DIVERSOS:
        return "Diversos"
    else:
        return "Tipo inválido"


class Mercado:
    """
    Classe base com as operações do mercado, independentes da estrutura usada.

    Cada árvore (ABB Iterativa / AVL Recursiva) herda desta classe e implementa:
      - vazia(), cheia(), tamanho()
      - insere(item) e remove(nome)
      - _buscaNo(nome): devolve o nó que guarda o item de nome *nome* (ou None)
      - _iniciaPercurso() e _proximoNo(): percorrem os nós em ordem alfabética de nome.
        _iniciaPercurso() prepara o percurso e cada chamada a _proximoNo() devolve o
        próximo nó (ou None quando acabar)
    O resto (buscar, atualiza, vendas, relatórios...) é feito aqui, em cima disso.
    """

    # ---- a implementar nas subclasses ----
    def vazia(self) -> bool:
        raise NotImplementedError

    def cheia(self) -> bool:
        raise NotImplementedError

    def tamanho(self) -> int:
        raise NotImplementedError

    def insere(self, item: TipoItem) -> bool:
        raise NotImplementedError

    def remove(self, nome: str) -> bool:
        raise NotImplementedError

    def _buscaNo(self, nome: str):
        raise NotImplementedError

    def _iniciaPercurso(self) -> None:
        raise NotImplementedError

    def _proximoNo(self):
        raise NotImplementedError

    def buscar(self, nome: str) -> TipoItem | None:
        """
        Busca um item na estrutura e retorna uma cópia do item ou None caso não encontrado
        """

        if self.vazia():
            return None

        no = self._buscaNo(nome)

        if no == None:
            return None

        return deepcopy(no.item)

    def registraVenda(self, nome: str, quantidade: int) -> bool:
        """
        Registra um venda de um produto com uma quantidade informada
        """
        if self.vazia():
            return False

        if quantidade <= 0:
            return False

        no = self._buscaNo(nome)

        if no == None:
            return False

        if no.item.quantidade_estoque < quantidade:
            return False

        no.item.quantidade_estoque -= quantidade
        no.item.quantidade_vendida += quantidade

        no.item.total_bruto += quantidade * no.item.valor_venda
        no.item.total_liquido += quantidade * (no.item.valor_venda - no.item.valor_custo)

        return True

    def atualiza(self, itemAtualizado: TipoItem) -> bool:
        """
        Atualiza os dados de algum item na estrutura
        """
        if self.vazia():
            return False

        no = self._buscaNo(itemAtualizado.nome)

        if no == None:
            return False

        no.item.tipo = itemAtualizado.tipo
        no.item.quantidade_estoque = itemAtualizado.quantidade_estoque
        no.item.valor_custo = itemAtualizado.valor_custo
        no.item.valor_venda = itemAtualizado.valor_venda

        return True

    def relatorioEstoqueTotal(self) -> None:
        """
        Imprime todos os itens que estão em estoque
        """
        if self.vazia():
            print("Sem produtos!")
            return

        primeiro = True

        print("Relatório de produtos em estoque: ")
        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            if no.item.quantidade_estoque > 0:
                if not primeiro:
                    print(", ", end="")
                print(no.item.nome, end="")
                primeiro = False
            no = self._proximoNo()

        if primeiro:
            print("Nenhum produto em estoque.")

        print()

    def relatorioEstoqueTipo(self, tipo: int) -> None:
        """
        Imprime todos os itens de *tipo* que estão em estoque
        """
        if self.vazia():
            print("Sem produtos!")
            return

        print(f"Relatório de produtos em estoque do tipo {mostrarTipo(tipo)}: ")
        primeiro = True
        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            if no.item.tipo == tipo and no.item.quantidade_estoque > 0:
                if not primeiro:
                    print(", ", end="")
                print(no.item.nome, end="")
                primeiro = False
            no = self._proximoNo()

        if primeiro:
            print(f"Nenhum produto do tipo {mostrarTipo(tipo)}")

        print()

    def relatorioProdutosEsgotados(self) -> None:
        """
        Imprime todos os itens com estoque igual a 0
        """
        if self.vazia():
            print("Sem produtos!")
            return

        primeiro = True

        print("Relatório de produtos esgotados: ")
        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            if no.item.quantidade_estoque == 0:
                if not primeiro:
                    print(", ", end="")
                print(no.item.nome, end="")
                primeiro = False
            no = self._proximoNo()

        if primeiro:
            print("Nenhum produto esgotado.")

        print()

    def relatorioProdutosEstoqueBaixo(self, limite: int) -> None:
        """
        Imprime os itens que estão com estoque abaixo de *limite*
        """
        if self.vazia():
            print("Sem produtos!")
            return

        if limite < 0:
            print("Limite inválido.")
            return

        print(f"Relatório de produtos com estoque abaixo de {limite}: ")
        primeiro = True
        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            if no.item.quantidade_estoque < limite:
                if not primeiro:
                    print(", ", end="")
                print(no.item.nome, end="")
                primeiro = False
            no = self._proximoNo()

        if primeiro:
            print(f"Nenhum produto com estoque abaixo de {limite}")

        print()

    def relatorioQuantidadeVendida(self) -> None:
        """
        Imprime os itens que foram vendidos e a quantidade vendida
        """
        if self.vazia():
            print("Sem produtos!")
            return

        print("Relatório de quantidade vendida: ")
        primeiro = True
        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            if no.item.quantidade_vendida > 0:
                if not primeiro:
                    print(", ", end="")
                print(f"{no.item.nome} ({no.item.quantidade_vendida})", end="")
                primeiro = False
            no = self._proximoNo()

        if primeiro:
            print("Nenhum produto vendido.")

        print()

    def relatorioTotalBruto(self) -> None:
        """
        Imprime o total bruto de vendas
        """
        if self.vazia():
            print("Sem produtos!")
            return

        total_bruto = 0.0

        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            total_bruto += no.item.total_bruto
            no = self._proximoNo()

        print(f"Relatório de total bruto: R$ {total_bruto:.2f}")

    def relatorioTotalLiquido(self) -> None:
        """
        Imprime o total líquido de vendas
        """
        if self.vazia():
            print("Sem produtos!")
            return

        total_liquido = 0.0

        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            total_liquido += no.item.total_liquido
            no = self._proximoNo()

        print(f"Relatório de total líquido: R$ {total_liquido:.2f}")

    def reajustePercentual(self, percentual: float) -> None:
        """
        Reajusta o preço de todos os itens
        """
        if self.vazia():
            print("Sem produtos!")
            return

        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            no.item.valor_venda *= 1 + percentual / 100
            no = self._proximoNo()

    def mostra(self) -> None:
        """
        Imprime o nome de todos os itens em ordem alfabética, numerados
        """
        contador = 1

        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            print(f"{contador} - {no.item.nome}")
            no = self._proximoNo()
            contador += 1

    def reiniciaVendas(self) -> None:
        """
        Reinicia todos os dados de vendas
        """
        self._iniciaPercurso()
        no = self._proximoNo()
        while no != None:
            no.item.quantidade_vendida = 0
            no.item.total_bruto = 0.0
            no.item.total_liquido = 0.0
            no = self._proximoNo()