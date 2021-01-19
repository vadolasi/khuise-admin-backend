from django.contrib.postgres.fields import ArrayField
from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    price = models.FloatField('preço')
    description = models.TextField('descrição')

    images = ArrayField(models.ImageField(), verbose_name='imagens')

    stock = models.JSONField()
    categories = ArrayField(
        models.CharField(
            max_length=255,
        ), verbose_name='categorias',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
