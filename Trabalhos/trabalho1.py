# Henrique Tutomu Sagawa - RA152725

from copy import deepcopy
from dataclasses import dataclass


@dataclass
class TipoItem:
    nome: str = ""
    tipo: int = 0
    quantidade_estoque: int = 0
    quantidade_vendida: int = 0
    valor_custo: float = 0.0
    valor_venda: float = 0.0
    total_bruto: float = 0.0
    total_liquido: float = 0.0


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
        self._inicio: No | None = None
        self._nItens: int = 0

    def vazia(self):
        return self._inicio == None

    def cheia(self):
        return False

    def tamanho(self):
        return self._nItens

    def _buscaAnterior(self, nome: str) -> No | None:
        anterior = None
        atual = self._inicio

        while atual != None and atual.item.nome.lower() < nome.lower():
            anterior = atual
            atual = atual.prox

        return anterior

    def insere(self, item: TipoItem) -> bool:
        anterior = self._buscaAnterior(item.nome)

        if anterior == None:
            atual = self._inicio
        else:
            atual = anterior.prox

        if atual != None and atual.item.nome.lower() <= item.nome.lower():
            return False

        novo_no = No(deepcopy(item))

        if anterior == None:
            novo_no.prox = self._inicio
            self._inicio = novo_no
        else:
            novo_no.prox = anterior.prox
            anterior.prox = novo_no

        self._nItens += 1
        return True

    def remove(self, nome: str) -> bool:
        if self.vazia():
            return False

        anterior = self._buscaAnterior(nome)

        if anterior == None:
            atual = self._inicio
        else:
            atual = anterior.prox

        if atual == None or atual.item.nome.lower() != nome.lower():
            return False

        if anterior == None:
            self._inicio = atual.prox
        else:
            anterior.prox = atual.prox

        self._nItens -= 1
        return True

    def buscar(self, nome: str) -> TipoItem | None:
        if self.vazia():
            return None

        anterior = self._buscaAnterior(nome)

        if anterior == None:
            atual = self._inicio
        else:
            atual = anterior.prox

        if atual == None or atual.item.nome.lower() != nome.lower():
            return None

        return deepcopy(atual.item)

    def registraVenda(self, nome: str, quantidade: int) -> bool:
        if self.vazia():
            return False

        anterior = self._buscaAnterior(nome)

        if anterior == None:
            atual = self._inicio
        else:
            atual = anterior.prox

        if atual == None or atual.item.nome.lower() != nome.lower():
            return False

        if atual.item.quantidade_estoque < quantidade:
            return False

        atual.item.quantidade_estoque -= quantidade
        atual.item.quantidade_vendida += quantidade

        atual.item.total_bruto += quantidade * atual.item.valor_venda
        atual.item.total_liquido += quantidade * (atual.item.valor_venda - atual.item.valor_custo)

        return True

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

        if primeiro:
            print("Nenhum produto em estoque.")

        print()
        return

    def relatorioEstoqueTipo(self, tipo: int):
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        print(f"Relatório de produtos em estoque do tipo {mostrarTipo(tipo)}: ")
        primeiro = True
        while atual != None:
            if atual.item.tipo == tipo and atual.item.quantidade_estoque > 0:
                if not primeiro:
                    print(", ", end="")
                print(atual.item.nome, end="")
                primeiro = False
            atual = atual.prox

        if primeiro:
            print(f"Nenhum produto do tipo {mostrarTipo(tipo)}")

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

        if primeiro:
            print("Nenhum produto esgotado.")

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

        if primeiro:
            print(f"Nenhum produto com estoque abaixo de {limite}")

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

        if primeiro:
            print("Nenhum produto vendido.")

        print()

        return

    def relatorioTotalBruto(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio
        total_bruto = 0.0

        while atual != None:
            total_bruto += atual.item.total_bruto
            atual = atual.prox

        print(f"Relatório de total bruto: R$ {total_bruto:.2f}")

    def relatorioTotalLiquido(self) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio
        total_liquido = 0.0

        while atual != None:
            total_liquido += atual.item.total_liquido
            atual = atual.prox

        print(f"Relatório de total líquido: R$ {total_liquido:.2f}")

    def reajustePercentual(self, percentual: float) -> None:
        if self.vazia():
            print("Sem produtos!")
            return

        atual = self._inicio

        while atual != None:
            atual.item.valor_venda *= 1 + percentual / 100
            atual = atual.prox

    def mostra(self) -> None:
        atual = self._inicio

        contador = 1

        while atual != None:
            print(f"{contador} - {atual.item.nome}")
            atual = atual.prox
            contador += 1

    def atualiza(self, itemAtualizado: TipoItem) -> bool:
        if self.vazia():
            return False

        anterior = self._buscaAnterior(itemAtualizado.nome)

        if anterior == None:
            item = self._inicio
        else:
            item = anterior.prox

        if item == None or item.item.nome.lower() != itemAtualizado.nome.lower():
            return False

        item.item.tipo = itemAtualizado.tipo
        item.item.quantidade_estoque = itemAtualizado.quantidade_estoque
        item.item.quantidade_vendida = itemAtualizado.quantidade_vendida
        item.item.valor_custo = itemAtualizado.valor_custo
        item.item.valor_venda = itemAtualizado.valor_venda

        return True

    def reiniciaVendas(self) -> None:

        atual = self._inicio

        while atual != None:
            atual.item.quantidade_vendida = 0
            atual.item.total_bruto = 0.0
            atual.item.total_liquido = 0.0
            atual = atual.prox

def mostrarTipo(tipo: int) -> str:
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

def mostrarTipos() -> None:
    print("Tipos de produtos:")
    print(f"{ACOUGUE} - Açougue")
    print(f"{PADARIA} - Padaria")
    print(f"{FRIOSELATICINIOS} - Frios e Laticínios")
    print(f"{HIGIENECORPORAL} - Higiene e Corporal")
    print(f"{LIMPEZA} - Limpeza")
    print(f"{HORTIFRUTI} - Hortifruti")
    print(f"{GRAOSFARINACEOSECAFE} - Grãos, Farináceos e Café")
    print(f"{BEBIDAS} - Bebidas")
    print(f"{UTENSILIOS} - Utensílios")
    print(f"{DIVERSOS} - Diversos")

def cadastrarProduto(lista: ListaDinamicaEncadeada) -> None:
    print("\n=== CADASTRAR PRODUTO ===")
    nome = input("Digite o nome do produto: ")
    if not nome:
        print("Nome inválido. Produto não cadastrado.")
        return
    mostrarTipos()
    tipo = int(input("Digite o tipo do produto (1-10): "))
    if tipo < 1 or tipo > 10:
        print("Tipo inválido. Produto não cadastrado.")
        return
    quantidade_estoque = int(input("Digite a quantidade em estoque: "))
    if quantidade_estoque < 0:
        print("Quantidade inválida. Produto não cadastrado.")
        return
    valor_custo = float(input("Digite o valor de custo: "))
    if valor_custo < 0:
        print("Valor de custo inválido. Produto não cadastrado.")
        return
    valor_venda = float(input("Digite o valor de venda: "))
    if valor_venda < 0:
        print("Valor de venda inválido. Produto não cadastrado.")
        return

    item = TipoItem(
        nome=nome,
        tipo=tipo,
        quantidade_estoque=quantidade_estoque,
        quantidade_vendida=0,
        valor_custo=valor_custo,
        valor_venda=valor_venda,
    )

    if lista.insere(item):
        print(f"Produto '{nome}' cadastrado com sucesso!")
    else:
        print(f"Produto '{nome}' já existe na lista.")


def removerProduto(lista: ListaDinamicaEncadeada) -> None:
    print("\n=== REMOVER PRODUTO ===")
    nome = input("Digite o nome do produto a ser removido: ")

    if lista.remove(nome):
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print(f"Produto '{nome}' não encontrado na lista.")

def consultarProduto(lista: ListaDinamicaEncadeada) -> None:
    print("\n=== CONSULTAR PRODUTO ===")
    nome = input("Digite o nome do produto a ser consultado: ")

    item = lista.buscar(nome)

    if item != None:

        print(f"Nome: {item.nome}")
        print(f"Tipo: {mostrarTipo(item.tipo)}")
        print(f"Quantidade em estoque: {item.quantidade_estoque}")
        print(f"Quantidade vendida: {item.quantidade_vendida}")
        print(f"Valor de custo: {item.valor_custo}")
        print(f"Valor de venda: {item.valor_venda:.2f}")
    else:
        print(f"Produto '{nome}' não encontrado na lista.")

def atualizarProduto(lista: ListaDinamicaEncadeada) -> None:
    print("\n=== ATUALIZAR PRODUTO ===")
    nome = input("Digite o nome do produto a ser atualizado: ")

    item = lista.buscar(nome)

    if item != None:
        print(f"Nome: {item.nome}")
        print(f"Tipo: {mostrarTipo(item.tipo)}")
        print(f"Quantidade em estoque: {item.quantidade_estoque}")
        print(f"Quantidade vendida: {item.quantidade_vendida}")
        print(f"Valor de custo: {item.valor_custo}")
        print(f"Valor de venda: {item.valor_venda:.2f}")

        mostrarTipos()
        tipo = int(input("Digite o novo tipo do produto (1-10): "))
        if tipo < 1 or tipo > 10:
            print("Tipo inválido. Produto não atualizado.")
            return
        quantidade_estoque = int(input("Digite a nova quantidade em estoque: "))
        if quantidade_estoque < 0:
            print("Quantidade inválida. Produto não atualizado.")
            return
        valor_custo = float(input("Digite o novo valor de custo: "))
        if valor_custo < 0:
            print("Valor de custo inválido. Produto não atualizado.")
            return
        valor_venda = float(input("Digite o novo valor de venda: "))
        if valor_venda < 0:
            print("Valor de venda inválido. Produto não atualizado.")
            return

        itemAtualizado = TipoItem(
            nome=nome,
            tipo=tipo,
            quantidade_estoque=quantidade_estoque,
            quantidade_vendida=item.quantidade_vendida,
            valor_custo=valor_custo,
            valor_venda=valor_venda,
        )

        if lista.atualiza(itemAtualizado):
            print(f"Produto '{nome}' atualizado com sucesso!")
        else:
            print(f"Erro ao atualizar o produto '{nome}'.")
    else:
        print(f"Produto '{nome}' não encontrado na lista.")

def listarProdutos(lista: ListaDinamicaEncadeada) -> None:
    print("\n=== LISTAR PRODUTOS ===")
    lista.mostra()

def registraVenda(lista: ListaDinamicaEncadeada) -> None:
    print("\n=== REGISTRAR VENDA DE PRODUTO ===")
    nome = input("Digite o nome do produto a ser vendido: ")

    item = lista.buscar(nome)

    if item != None:
        print(f"Nome: {item.nome}")
        print(f"Tipo: {mostrarTipo(item.tipo)}")
        print(f"Quantidade em estoque: {item.quantidade_estoque}")
        print(f"Quantidade vendida: {item.quantidade_vendida}")
        print(f"Valor de custo: {item.valor_custo}")
        print(f"Valor de venda: {item.valor_venda:.2f}")

        quantidade = int(input("Digite a quantidade vendida: "))
        if quantidade <= 0:
            print("Quantidade inválida. Venda não registrada.")
            return

        if lista.registraVenda(nome, quantidade):
            print(f"Venda de {quantidade} unidade(s) do produto '{nome}' registrada com sucesso!")
        else:
            print(f"Erro ao registrar a venda do produto '{nome}'. Verifique o estoque disponível.")
    else:
        print(f"Produto '{nome}' não encontrado na lista.")

def main():
    lista = ListaDinamicaEncadeada()

    while True:
        print(
"""
========== CONTROLE DE SUPERMERCADO ==========
1 - Cadastrar produto
2 - Remover produto
3 - Consultar produto
4 - Listar todos os produtos
5 - Atualizar produto
6 - Relatório completo de estoque
7 - Relatório de estoque por tipo
8 - Relatório de produtos esgotados
9 - Relatório de produtos com estoque baixo
10 - Relatório de quantidade vendida
11 - Relatório de valor total bruto
12 - Relatório de valor total líquido
13 - Reajuste percentual dos preços de venda
14 - Registrar venda de produto
15 - Reiniciar vendas
0 - Sair
==============================================
""")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrarProduto(lista)
        elif opcao == 2:
            removerProduto(lista)
        elif opcao == 3:
            consultarProduto(lista)
        elif opcao == 4:
            listarProdutos(lista)
        elif opcao == 5:
            atualizarProduto(lista)
        elif opcao == 6:
            print("\n=== RELATÓRIO COMPLETO DE ESTOQUE ===")
            lista.relatorioEstoqueTotal()
        elif opcao == 7:
            print("\n=== RELATÓRIO DE ESTOQUE POR TIPO ===")
            mostrarTipos()
            tipo = int(input("Digite o tipo do produto (1-10): "))
            if tipo < 1 or tipo > 10:
                print("Tipo inválido.")
            else:
                lista.relatorioEstoqueTipo(tipo)
        elif opcao == 8:
            print("\n=== RELATÓRIO DE PRODUTOS ESGOTADOS ===")
            lista.relatorioProdutosEsgotados()
        elif opcao == 9:
            print("\n=== RELATÓRIO DE PRODUTOS COM ESTOQUE BAIXO ===")
            limite = int(input("Digite o limite de estoque: "))
            lista.relatorioProdutosEstoqueBaixo(limite)
        elif opcao == 10:
            print("\n=== RELATÓRIO DE QUANTIDADE VENDIDA ===")
            lista.relatorioQuantidadeVendida()
        elif opcao == 11:
            print("\n=== RELATÓRIO DE VALOR TOTAL BRUTO ===")
            lista.relatorioTotalBruto()
        elif opcao == 12:
            print("\n=== RELATÓRIO DE VALOR TOTAL LÍQUIDO ===")
            lista.relatorioTotalLiquido()
        elif opcao == 13:
            print("\n=== REAJUSTE PERCENTUAL DOS PREÇOS DE VENDA ===")
            percentual = float(input("Digite o percentual de reajuste: "))
            if percentual < -100:
                print("Percentual inválido.")
            else:
                lista.reajustePercentual(percentual)
                print("Valores reajustados.")
        elif opcao == 14:
            registraVenda(lista)
        elif opcao == 15:
            print("\n=== REINICIAR VENDAS ===")
            lista.reiniciaVendas()
            print("Vendas reiniciadas.")
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()