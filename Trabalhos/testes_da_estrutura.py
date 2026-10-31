import unittest
from io import StringIO
import sys

# Importa as estruturas do arquivo do aluno
from trabalho1 import (
    TipoItem,
    ListaDinamicaEncadeada,
    mostrarTipo,
    ACOUGUE,
    PADARIA,
    BEBIDAS,
    UTENSILIOS,
    DIVERSOS
)


class TestListaDinamicaEncadeada(unittest.TestCase):

    def setUp(self):
        """Inicializa uma nova lista antes de cada teste."""
        self.lista = ListaDinamicaEncadeada()
        # Correção: alterado GRAOS_FARINACEOS=7 para tipo=7
        self.item_a = TipoItem("Arroz", tipo=7, quantidade_estoque=10, quantidade_vendida=5, valor_custo=10.0, valor_venda=15.0)
        self.item_b = TipoItem("Banana", tipo=6, quantidade_estoque=0, quantidade_vendida=2, valor_custo=2.0, valor_venda=4.0)
        self.item_c = TipoItem("Carne", tipo=ACOUGUE, quantidade_estoque=5, quantidade_vendida=0, valor_custo=20.0, valor_venda=30.0)

    def test_lista_vazia_e_tamanho(self):
        """Testa estado inicial de lista vazia e contagem de itens."""
        self.assertTrue(self.lista.vazia())
        self.assertFalse(self.lista.cheia())
        self.assertEqual(self.lista.tamanho(), 0)

        self.lista.insere(self.item_a)
        self.assertFalse(self.lista.vazia())
        self.assertEqual(self.lista.tamanho(), 1)

    def test_insercao_ordenada_e_duplicados(self):
        """Testa se a inserção mantém a ordem alfabética e rejeita nomes duplicados."""
        # Inserção fora de ordem alfabética: Carne, depois Arroz, depois Banana
        self.assertTrue(self.lista.insere(self.item_c)) # Carne
        self.assertTrue(self.lista.insere(self.item_a)) # Arroz (deve ir para o início)
        self.assertTrue(self.lista.insere(self.item_b)) # Banana (deve ir para o meio)

        self.assertEqual(self.lista.tamanho(), 3)

        # Tentativa de inserir item com mesmo nome (case insensitive)
        item_duplicado = TipoItem("arroz", tipo=1, quantidade_estoque=5, quantidade_vendida=0, valor_custo=1.0, valor_venda=2.0)
        self.assertFalse(self.lista.insere(item_duplicado))
        self.assertEqual(self.lista.tamanho(), 3)

    def test_busca_existente_e_inexistente(self):
        """Testa a busca de elementos existentes e não existentes."""
        self.lista.insere(self.item_a)

        # Busca em lista com elemento (case insensitive)
        res_a = self.lista.buscar("ARROZ")
        self.assertIsNotNone(res_a)
        self.assertEqual(res_a.nome, "Arroz")

        # Verifica independência (deepcopy no retorno)
        res_a.quantidade_estoque = 999
        self.assertEqual(self.lista.buscar("Arroz").quantidade_estoque, 10)

        # Busca item inexistente
        self.assertIsNone(self.lista.buscar("Feijão"))

        # Busca em lista vazia
        lista_vazia = ListaDinamicaEncadeada()
        self.assertIsNone(lista_vazia.buscar("Arroz"))

    def test_remocao_inicio_meio_fim_e_inexistente(self):
        """Testa remoção nos diferentes nós da lista ligada."""
        # Preenche com 3 itens: Arroz, Banana, Carne
        self.lista.insere(self.item_b)
        self.lista.insere(self.item_a)
        self.lista.insere(self.item_c)

        # Remover elemento inexistente
        self.assertFalse(self.lista.remove("Detergente"))

        # Remover do meio (Banana)
        self.assertTrue(self.lista.remove("banana"))
        self.assertEqual(self.lista.tamanho(), 2)
        self.assertIsNone(self.lista.buscar("Banana"))

        # Remover do início (Arroz)
        self.assertTrue(self.lista.remove("Arroz"))
        self.assertEqual(self.lista.tamanho(), 1)
        self.assertIsNone(self.lista.buscar("Arroz"))

        # Remover do fim (Carne)
        self.assertTrue(self.lista.remove("Carne"))
        self.assertTrue(self.lista.vazia())
        self.assertEqual(self.lista.tamanho(), 0)

        # Remover em lista vazia
        self.assertFalse(self.lista.remove("Carne"))

    def test_atualiza(self):
        """Testa o método de atualização de dados de um produto."""
        self.lista.insere(self.item_a)

        # Atualização válida
        item_modificado = TipoItem("arroz", tipo=PADARIA, quantidade_estoque=50, quantidade_vendida=12, valor_custo=12.0, valor_venda=18.0)
        self.assertTrue(self.lista.atualiza(item_modificado))

        item_buscado = self.lista.buscar("Arroz")
        self.assertEqual(item_buscado.tipo, PADARIA)
        self.assertEqual(item_buscado.quantidade_estoque, 50)
        self.assertEqual(item_buscado.quantidade_vendida, 12)
        self.assertEqual(item_buscado.valor_custo, 12.0)

        # Atualizar produto inexistente
        item_inexistente = TipoItem("Leite", tipo=PADARIA, quantidade_estoque=10, quantidade_vendida=0, valor_custo=2.0, valor_venda=3.0)
        self.assertFalse(self.lista.atualiza(item_inexistente))

        # Atualizar em lista vazia
        lista_vazia = ListaDinamicaEncadeada()
        self.assertFalse(lista_vazia.atualiza(item_modificado))

    def test_reajuste_percentual_e_reinicia_vendas(self):
        """Testa os métodos que alteram valores/vendas em massa."""
        self.lista.insere(self.item_a) # v_venda: 15.0, q_vendida: 5
        self.lista.insere(self.item_b) # v_venda: 4.0, q_vendida: 2

        # Teste reajuste de +10%
        self.lista.reajustePercentual(10.0)
        self.assertAlmostEqual(self.lista.buscar("Arroz").valor_venda, 16.5)
        self.assertAlmostEqual(self.lista.buscar("Banana").valor_venda, 4.4)

        # Teste reiniciar vendas
        self.lista.reiniciaVendas()
        self.assertEqual(self.lista.buscar("Arroz").quantidade_vendida, 0)
        self.assertEqual(self.lista.buscar("Banana").quantidade_vendida, 0)

    def test_relatorios_calculos_financeiros(self):
        """Testa captura dos prints e cálculos de total bruto/líquido."""
        self.lista.insere(self.item_a) # vendida: 5, custo: 10, venda: 15 -> Bruto=75, Líquido=25
        self.lista.insere(self.item_b) # vendida: 2, custo: 2, venda: 4   -> Bruto=8,  Líquido=4

        # Redireciona o stdout para capturar saídas dos relatórios
        stdout_original = sys.stdout
        sys.stdout = buffer = StringIO()

        try:
            self.lista.relatorioTotalBruto()
            saida_bruto = buffer.getvalue()
            self.assertIn("R$ 83.00", saida_bruto)

            buffer.seek(0)
            buffer.truncate(0)

            self.lista.relatorioTotalLiquido()
            saida_liquido = buffer.getvalue()
            self.assertIn("R$ 29.00", saida_liquido)

        finally:
            sys.stdout = stdout_original

    def test_relatorios_saida_texto(self):
        """Testa o comportamento dos relatórios de listagem e estoque."""
        self.lista.insere(self.item_a) # estoque: 10
        self.lista.insere(self.item_b) # estoque: 0 (esgotado)

        stdout_original = sys.stdout
        sys.stdout = buffer = StringIO()

        try:
            # Teste estoque esgotado
            self.lista.relatorioProdutosEsgotados()
            self.assertIn("Banana", buffer.getvalue())

            buffer.seek(0)
            buffer.truncate(0)

            # Teste estoque baixo com limite 5 (apenas Banana < 5)
            self.lista.relatorioProdutosEstoqueBaixo(5)
            self.assertIn("Banana", buffer.getvalue())
            self.assertNotIn("Arroz", buffer.getvalue())

        finally:
            sys.stdout = stdout_original

    def test_funcao_auxiliar_mostrar_tipo(self):
        """Testa conversão dos inteiros para nomes de tipos de produtos."""
        self.assertEqual(mostrarTipo(ACOUGUE), "Açougue")
        self.assertEqual(mostrarTipo(PADARIA), "Padaria")
        self.assertEqual(mostrarTipo(99), "Tipo inválido")


if __name__ == "__main__":
    unittest.main()