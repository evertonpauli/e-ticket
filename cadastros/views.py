from django.shortcuts import render
from rest_framework import response, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError

# Create your views here.
from cadastros.serializers import *

class ClientesViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Clientes
    """
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

# --------------------------------------------------

class CategoriaViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Categoria
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# --------------------------------------------------

class StatusViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Status
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# --------------------------------------------------