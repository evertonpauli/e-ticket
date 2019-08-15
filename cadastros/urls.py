from rest_framework import routers

from cadastros.views import ClientesViewSet, CategoriaViewSet, StatusViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register('clientes', ClientesViewSet)
router.register('categorias', CategoriaViewSet)
router.register('status', StatusViewSet)

urlpatterns = router.urls
