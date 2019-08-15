from rest_framework import routers

from movimentos.views import ChamadoViewSet, BaseConhecimentoViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register('chamados', ChamadoViewSet)
router.register('baseconhecimentos', BaseConhecimentoViewSet)

urlpatterns = router.urls
