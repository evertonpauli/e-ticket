from rest_framework import serializers
from .models import *


class EmpresaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Empresa
    """

    class Meta:
        model = Empresa
        fields = "__all__"


# -----------------------------------------------------------------------------


class ModulosSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Modulos
    """

    class Meta:
        model = Modulos
        fields = "__all__"


# -----------------------------------------------------------------------------

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'

# -----------------------------------------------------------------------------
