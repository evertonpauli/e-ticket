from django.test import TestCase
from .models import *

# ------------------------------------------------------------------------------

class TestClientes(TestCase):
    #  Teste para Clientes da Empresa

    def test_add_cliente(self):
        cli = Clientes()

        cli.razao_social = 'Everton Aloisio Pauli'
        cli.nome_fantasia = 'Everton Pauli'
        cli.cnpj = '023.363.311-10'
        cli.cep = '78365-000'
        cli.endereco = 'Av Lions Internacional'
        cli.numero = '550SW'
        cli.bairro = 'Centro'
        cli.municipio = 'Sapezal'
        cli.estado = 'MT'
        
        cli.save()

        self.assertEqual(str(cli), str(cli.id), 'Verificar __str__do objeto')  
        self.assertEqual(cli.pk, 1, 'Verifica se salvou no banco')        

    def test_altera_cliente(self):
        cli = Clientes()

        cli.razao_social = 'Nome completo do Cliente'
        cli.nome_fantasia = 'Nome Abreviado'
        cli.cnpj = '015.697.694-10'
        cli.cep = '78365-000'
        cli.endereco = 'Av Lions'
        cli.numero = '550SW'
        cli.bairro = 'Centro'
        cli.municipio = 'Cuiaba'
        cli.estado = 'MT'
        
        cli.save()
 
        self.assertEqual(str(cli), str(cli.id), 'Verificar __str__do objeto')  
        self.assertEqual(cli.pk, 1, 'Verifica se salvou no banco')

# ------------------------------------------------------------------------------

class TestCategoria(TestCase):
    #  Teste para Categoria

    def test_add_categoria(self):
        ca = Categoria()

        ca.descricao = 'Categoria 1'

        ca.save()

        self.assertEqual(str(ca), str(ca.id), 'Verifica o __str__')
        self.assertEqual(ca.pk, 1, 'Verifica se salvou')

    def test_altera_categoria(self):
        ca = Categoria()

        ca.descricao = 'Category 2'

        ca.save()

        self.assertEqual(str(ca), str(ca.id), 'Verifica o __str__')
        self.assertEqual(ca.pk, 1, 'Verifica se salvou')        

# ------------------------------------------------------------------------------        

class TestStatus(TestCase):
    #  teste para Status

    def test_add_status(self):
        st = Status()

        st.descricao = 'Descricao Status 01'

        st.save()

        self.assertEqual(str(st), str(st.id), 'Verifica o __str__')
        self.assertEqual(st.pk, 1, 'Verifica o save no banco')

    def test_altera_status(self):
        st = Status()
    
        st.descricao = 'Descricao Status 01'
    
        st.save()
    
        self.assertEqual(str(st), str(st.id), 'Verifica o __str__')
        self.assertEqual(st.pk, 1, 'Verifica o save no banco')        

# ------------------------------------------------------------------------------        

#  fim * 