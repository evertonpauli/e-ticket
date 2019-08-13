from django.shortcuts import render
from rest_framework import response, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError

# Create your views here.
from movimentos.serializers import *

class ChamadoViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Chamado
    """
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

# --------------------------------------------------

class BaseConhecimentoViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de BaseConhecimento
    """
    queryset = BaseConhecimento.objects.all()
    serializer_class = BaseConhecimentoSerializer

# --------------------------------------------------
