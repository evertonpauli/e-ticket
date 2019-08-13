from django.shortcuts import render
from rest_framework import response, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError

# Create your views here.
from base.serializers import *

class EmpresaViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Empresa
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

# --------------------------------------------------

class ModulosViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Modulos
    """
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer

# --------------------------------------------------

class UsuarioViewSet(viewsets.ViewSet):
    """
    Viewset para modelo de Usuarios
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# --------------------------------------------------