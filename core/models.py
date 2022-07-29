from django.db import models
from django.db.models import CheckConstraint


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.ForeignKey('Fabricante', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Fabricante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)

    # TODO: Implementar o CheckConstraint
    # class Meta:
    #     constraints = [
    #         CheckConstraint(check=models.Q(categoria__fabricante=models.F(
    #             'fabricante')), name='categoria_fabricante_check')
    #     ]

    def __str__(self):
        return self.nome
