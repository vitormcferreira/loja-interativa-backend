from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'fabricantes', views.FabricanteViewSet)
router.register(r'produtos', views.ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categorias_da_fabricante/<int:fabricante_id>/',
         views.categorias_da_fabricante),

    # Documentação
    path('schema/', SpectacularAPIView().as_view(), name='schema'),
    # link para a visualização da API
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
