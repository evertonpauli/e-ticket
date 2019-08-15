from base.models import *
from rest_framework import viewsets
from base.serializers import *


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Empresa
    """

    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


# --------------------------------------------------


class ModulosViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Modulos
    """

    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer


# --------------------------------------------------


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Usuarios
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# --------------------------------------------------
