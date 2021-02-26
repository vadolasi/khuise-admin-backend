"""
from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('nome', max_length=30)


class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    price = models.FloatField('preço')
    description = models.TextField('descrição')
    realese_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        # app_label = 'products'

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='produto',
        related_name='images',
    )
    image = models.ImageField()  # storage=grid_fs_storage)

    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'
        # app_label = 'products'


class Color(models.Model):
    color = models.CharField('cor', max_length=20)


class Size(models.Model):
    size = models.CharField('tamanho', max_length=2)


class Stock(models.Model):
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name='stock_colors',
        # related_name='stocks',
    )
    size = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name='tamanho',
        related_name='stock_sizes',
    )
    quantity = models.IntegerField('quantidade')

    class Meta:
        verbose_name = 'estoque'
        verbose_name_plural = 'estoque'
        # app_label = 'products'
"""

from django.conf import settings
from django.utils import timezone
from django.db import models
# from djongo.storage import GridFSStorage

# grid_fs_storage = GridFSStorage(collection='products_files')


class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    price = models.FloatField('preço')
    description = models.TextField('descrição')
    realese_date = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        # app_label = 'products'

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='produto',
        related_name='images',
    )
    image = models.ImageField()  # storage=grid_fs_storage)

    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'
        # app_label = 'products'


class Stock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='produto',
        related_name='stock',
    )
    color = models.CharField('cor', max_length=30)
    size = models.CharField('tamanho', max_length=2)
    stock = models.IntegerField('estoque')

    class Meta:
        verbose_name = 'estoque'
        verbose_name_plural = 'estoque'
        # app_label = 'products'


class Category(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField('nome', max_length=30)

