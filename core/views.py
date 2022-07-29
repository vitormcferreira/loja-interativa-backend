from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema_view, extend_schema
from core.serializers import CategoriaSerializer, FabricanteSerializer, ProdutoSerializer

from .models import Categoria, Fabricante, Produto


@extend_schema_view(
    list=extend_schema(summary='Obtém todas as categorias.'),
    create=extend_schema(summary='Insere uma nova categoria.'),
    retrieve=extend_schema(summary='Obtém uma categoria.'),
    update=extend_schema(summary='Atualiza uma categoria.'),
    partial_update=extend_schema(
        summary='Atualiza parcialmente uma categoria.'),
    destroy=extend_schema(summary='Remove uma categoria.'),
)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer


@extend_schema_view(
    list=extend_schema(summary='Obtém todas as fabricantes.'),
    create=extend_schema(summary='Insere uma nova fabricante.'),
    retrieve=extend_schema(summary='Obtém uma fabricante.'),
    update=extend_schema(summary='Atualiza uma fabricante.'),
    partial_update=extend_schema(
        summary='Atualiza parcialmente uma fabricante.'),
    destroy=extend_schema(summary='Remove uma fabricante.'),
)
class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = Fabricante.objects.all().order_by('nome')
    serializer_class = FabricanteSerializer


@extend_schema_view(
    list=extend_schema(summary='Obtém todos os produtos.'),
    create=extend_schema(summary='Insere um novo produto.'),
    retrieve=extend_schema(summary='Obtém um produto.'),
    update=extend_schema(summary='Atualiza um produto.'),
    partial_update=extend_schema(summary='Atualiza parcialmente um produto.'),
    destroy=extend_schema(summary='Remove um produto.'),
)
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer


# TODO: Documentação
@extend_schema(
    summary='Obtém todas as categorias de um fabricante.',
)
@api_view(['GET'])
def categorias_da_fabricante(request: Request, fabricante_id: int) -> Response:
    categorias = Categoria.objects.filter(
        fabricante__id=fabricante_id).order_by('name')
    serializer = CategoriaSerializer(categorias, many=True)

    return Response(serializer.data)
