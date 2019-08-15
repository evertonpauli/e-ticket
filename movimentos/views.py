from movimentos.models import *
from rest_framework import viewsets
from movimentos.serializers import *


class ChamadoViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de Chamado
    """

    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer


# --------------------------------------------------


class BaseConhecimentoViewSet(viewsets.ModelViewSet):
    """
    Viewset para modelo de BaseConhecimento
    """

    queryset = BaseConhecimento.objects.all()
    serializer_class = BaseConhecimentoSerializer


# --------------------------------------------------
