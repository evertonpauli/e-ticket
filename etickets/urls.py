from django.contrib import admin
from django.urls import path, include

from base.urls import EmpresaViewSet, ModulosViewSet, UsuarioViewSet
from cadastros.urls import ClientesViewSet, CategoriaViewSet
from movimentos.urls import ChamadoViewSet, BaseConhecimentoViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('base.urls')),
    path('cadastros/', include('cadastros.urls')),
    path('movimentos/', include('movimentos.urls')),

]
