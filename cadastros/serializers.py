from rest_framework import serializers

from .models import *


class ClientesSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Clientes
    """

    class Meta:
        model = Clientes
        fields = "__all__"


# -----------------------------------------------------------------------------


class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Categoria
    """

    class Meta:
        model = Categoria
        fields = "__all__"


# -----------------------------------------------------------------------------


class StatusSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Status
    """

    class Meta:
        model = Status
        fields = "__all__"


# -----------------------------------------------------------------------------
