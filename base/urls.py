from rest_framework import routers

from base.views import EmpresaViewSet, ModulosViewSet, UsuarioViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register('empresas', EmpresaViewSet)
router.register('modulos', ModulosViewSet)
router.register('usuario', UsuarioViewSet)

urlpatterns = router.urls
