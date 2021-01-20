from django.contrib.postgres.fields import ArrayField
from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    price = models.FloatField('preço')
    description = models.TextField('descrição')

    categories = ArrayField(
        models.CharField(
            max_length=255,
        ), verbose_name='categorias',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name='produto',
        related_name='images'
    )
    image = models.ImageField()


class ProductStock(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name='produto',
        related_name='stocks'
    )
    color = models.CharField('cor', max_length=30)
    size = models.CharField('tamanho', max_length=2)
    stock = models.IntegerField('estoque')
