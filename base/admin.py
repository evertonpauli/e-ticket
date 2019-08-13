from django.contrib import admin
from .models import *
from django.forms import ALL_FIELDS
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _



class ModulosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Modulos, ModulosAdmin)


class EmpresaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Empresa, EmpresaAdmin)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
   fieldsets = (
       (None, {'fields': ('username', 'password')}),
       (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
       (_('Custom info'), {'fields': (
           'cliente', 'suporte', 'desenvolvedor')}),
       (_('Permissions'), {
           'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
       }),
       (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
   )
    