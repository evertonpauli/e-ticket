from cadastros.serializers import *
from cadastros.models import *
from rest_framework import viewsets


class ClientesViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Clientes
    """

    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


# --------------------------------------------------


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Categoria
    """

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# --------------------------------------------------


class StatusViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Status
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# --------------------------------------------------
