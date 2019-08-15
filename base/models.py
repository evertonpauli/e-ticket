from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.


class Empresa(models.Model):
    """
    Modelo para guardar dados da empresa
    """

    razao_social = models.CharField(max_length=80, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=80, verbose_name="Nome Fantasia")
    cnpj = models.CharField(max_length=20, verbose_name="CNPJ/CPF")
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return f"{self.pk}"


# ------------------------------------------------------------------------------


class Modulos(models.Model):
    """
    Modelo para guardar dados de Módulos
    """

    descricao = models.CharField(max_length=80, verbose_name="Descrição")

    class Meta:
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"

    def __str__(self):
        return f"{self.pk}"


# ------------------------------------------------------------------------------


class Usuario(AbstractUser):
    """
    Modelo para vincular ao cadastro de Usuario do Django
    """

    cliente = models.BooleanField(default=False)
    suporte = models.BooleanField(default=False, verbose_name="suporte técnico")
    desenvolvedor = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username


# ------------------------------------------------------------------------------
