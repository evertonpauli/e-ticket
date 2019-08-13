from django.db import models

class Clientes(models.Model):
    """
    Modelo para guardar dados de Clientes
    """
    
    razao_social = models.CharField(max_length=80, verbose_name='Razão Social')
    nome_fantasia = models.CharField(max_length=80, verbose_name='Nome Fantasia')
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ/CPF')
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f'{self.pk}'

# ------------------------------------------------------------------------------

class Categoria(models.Model):
    """
    Modelo para guardar dados de Categoria
    """
    
    descricao = models.CharField(max_length=80, verbose_name='Categoria')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f'{self.pk}'

# ------------------------------------------------------------------------------

class Status(models.Model):
    """
    Modelo para guardar dados de Status
    """
    
    descricao = models.CharField(max_length=80, verbose_name='Status')

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return f'{self.pk}'

      