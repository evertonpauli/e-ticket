from django.test import TestCase

from .models import *


class TestUsuario(TestCase):
    #  Test de user

    def test_add_user(self):
        c = Usuario()

        c.cliente = "False"
        c.suporte = "True"
        c.desenvolvedor = "False"

        c.save()

        self.assertEqual(c.pk, 1, "Verifica se salvou")

    def test_alter_user(self):
        c = Usuario()

        c.cliente = "False"
        c.suporte = "False"
        c.desenvolvedor = "True"

        c.save()

        self.assertEqual(c.pk, 1, "Verifica se salvou")


# ------------------------------------------------------------------------------


class TestModulos(TestCase):
    #  Teste de Modulos

    def test_add_modulos(self):
        m = Modulos()

        m.descricao = "Financeiro"

        m.save()

        self.assertEqual(str(m), str(m.id), "Verificar __str__do objeto")
        self.assertEqual(m.pk, 1, "Verifica se salvou")

    def test_altera_modulos(self):
        m = Modulos()

        m.descricao = "Faturamento"

        m.save()

        self.assertEqual(str(m), str(m.id), "Verificar __str__do objeto")
        self.assertEqual(m.pk, 1, "Verifica se salvou")


# ------------------------------------------------------------------------------


class TestEmpresa(TestCase):
    #  Teste para Empresa

    def test_add_empresa(self):
        e = Empresa()

        e.razao_social = "Tininho Contabilidade Eireli ME"
        e.nome_fantasia = "Tininho Contabilidade"
        e.cnpj = "12.029.590/0001-64"
        e.cep = "78365-000"
        e.endereco = "Av Lions Internacional"
        e.numero = "550SW"
        e.bairro = "Centro"
        e.municipio = "Sapezal"
        e.estado = "MT"

        e.save()

        # Vem com o Galleti isso.
        self.assertEqual(str(e), str(e.id), "Verificar __str__do objeto")
        self.assertEqual(e.pk, 1, "Verifica se salvou no banco")

    def test_altera_empresa(self):
        e = Empresa()

        e.razao_social = "HiFuzion Fabrica de Softwares"
        e.nome_fantasia = "HiFuzion SoftHouse"
        e.cnpj = "21.456.123/0001-20"
        e.cep = "78365-000"
        e.endereco = "Av Internacional"
        e.numero = "159SW"
        e.bairro = "Zequinha"
        e.municipio = "Sapezal"
        e.estado = "MT"

        e.save()

        self.assertEqual(str(e), str(e.id), "Verificar __str__do objeto")
        self.assertEqual(e.pk, 1, "Verifica se salvou no banco")


# ------------------------------------------------------------------------------
