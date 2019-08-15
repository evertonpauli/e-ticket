from django.contrib import admin
from .models import *
from django.forms import ALL_FIELDS


class ChamadoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chamado, ChamadoAdmin)


class BaseConhecimentoAdmin(admin.ModelAdmin):
    pass


admin.site.register(BaseConhecimento, BaseConhecimentoAdmin)
