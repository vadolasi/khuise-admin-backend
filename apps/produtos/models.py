from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preço = models.FloatField()
    descrição = models.TextField()

    cor = models.CharField(max_length=255)

    imagem = models.ImageField(blank=True)

    stock = models.JSONField()
    categories = models.CharField(max_length=255);

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
