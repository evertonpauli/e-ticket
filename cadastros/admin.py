from django.contrib import admin
from .models import *
from django.forms import ALL_FIELDS


class ClientesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Clientes, ClientesAdmin)


class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status, StatusAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categoria, CategoriaAdmin)
