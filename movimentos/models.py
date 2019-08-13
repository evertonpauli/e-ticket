from django.db import models
# from base.models import Usuario
from cadastros.models import Clientes, Status, Categoria

class Chamado(models.Model):
    """
    Modelo para guardar dados de Chamados
    """

    BAIXA = 'Baixa'
    MEDIA = 'Média'
    ALTA = 'Alta'

    PRIORIDADE = (
        (BAIXA, 'Baixa'),
        (MEDIA, 'Média'),
        (ALTA, 'Alta'),
    )

    ABERTO = 'Aberto'
    AGUARDANDO_DEV = 'Aguardando Suporte'
    AGUARDANDO_SUP = 'Aguardando Desenvolvimento'
    CONCLUIDO = 'Concluido'

    SITUACAO = (
        (ABERTO, 'Aberto'),
        (AGUARDANDO_DEV, 'Aguardando Suporte'),
        (AGUARDANDO_SUP, 'Aguardando Desenvolvimento'),
        (CONCLUIDO, 'Concluido'),
    )

    data_chamado = models.DateField(auto_now=True)
    parceiro = models.ForeignKey(to='cadastros.Clientes', verbose_name='Nome do Parceiro',
                                on_delete=models.DO_NOTHING)
    contato = models.CharField(max_length=25, help_text='Contato')                              
    descricao = models.CharField(max_length=300, verbose_name='Descrição da Solicitação')
    prioridade = models.CharField(max_length=15,
                                verbose_name='Prioridade',
                                choices=PRIORIDADE)
    atendente = models.ForeignKey(to='base.Usuario', verbose_name='Usuario',
                                on_delete=models.DO_NOTHING)
    status = models.ForeignKey(to='cadastros.Status', verbose_name='Status',
                                on_delete=models.DO_NOTHING) 
    categoria = models.ForeignKey(to='cadastros.Categoria', verbose_name='Categoria',
                                on_delete=models.DO_NOTHING)  
    situacao = models.CharField(max_length=15,
                                verbose_name='Situação',
                                choices=SITUACAO)    
    data_conclusao = models.DateField(blank=True, null=True,
                                help_text='Preencha quando entregar alguma solicitação que ficou pendente.')
    obs_fechamento = models.TextField(max_length=300, blank=True, null=True,
                                help_text='Conclusão do atendimento. Máx.: 300 digitos')
    # anexos = models.FileField(upload_to='anexos/', null=True, blank=True)

 
    
    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        
# ------------------------------------------------------------------------------

class BaseConhecimento(models.Model):
    """
    Modelo para guardar dados de BaseConhecimento
    """
    
    BASICO = 'Basico'
    INTERMEDIARIO = 'Intermediario'
    AVANCADO = 'Avancado'

    NIVEL = (
        (BASICO, 'Basico'),
        (INTERMEDIARIO, 'Intermediario'),
        (AVANCADO, 'Avancado'),
    )

    descricao = models.CharField(max_length=80, verbose_name='Descrição')
    nivel = models.CharField(max_length=15,
                                          verbose_name='Nivel do User',
                                          choices=NIVEL, blank=True, null=True)

    class Meta:
        verbose_name = "Base de Conhecimento"
        verbose_name_plural = "Bases de Conhecimentos"

    def __str__(self):
        return f'{self.pk}'
       