from rest_framework import serializers

from .models import *

class ChamadoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Chamado
    """

    class Meta:
        model = Chamado
        fields = '__all__'

# -----------------------------------------------------------------------------

class BaseConhecimentoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo BaseConhecimento
    """

    class Meta:
        model = BaseConhecimento
        fields = '__all__'

# -----------------------------------------------------------------------------
