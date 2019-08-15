from django.test import TestCase
from .models import *

from cadastros.models import *

# Movimentos -------------------------------------------------------------------


class TestChamado(TestCase):
    fixtures = ["test_chamados"]

    def test_add_chamado(self):
        ch = Chamado()

        ch.data_chamado = "01/01/2019"
        ch.parceiro_id = 1
        ch.contato = "Clenildo"
        ch.descricao = "Enxendo as bolotas"
        ch.prioridade = Chamado.BAIXA
        ch.atendente_id = 2
        ch.status_id = 1
        ch.categoria_id = 1
        ch.situacao = Chamado.AGUARDANDO_DEV
        ch.data_conclusao = "2019-01-05"

        ch.save()

        self.assertEqual(str(ch), str(ch.id), "Verificar o __str__")
        self.assertEqual(ch.pk, 1, "Verifica se salvou")


# ------------------------------------------------------------------------------


class TestBaseConhecimento(TestCase):
    #  Test para base de conhecimento

    def test_add_baseconhecimento(self):
        bc = BaseConhecimento()

        bc.descricao = "Minima"
        bc.nivel = "BASICO"

        bc.save()

        self.assertEqual(str(bc), str(bc.id), "Verifica o __str__")
        self.assertEqual(bc.pk, 1, "Verifica se salvou")

    def test_altera_baseconhecimento(self):
        bc = BaseConhecimento()

        bc.descricao = "Boa"
        bc.nivel = "AVANCADO"

        bc.save()

        self.assertEqual(str(bc), str(bc.id), "Verifica o __str__")
        self.assertEqual(bc.pk, 1, "Verifica se salvou")
