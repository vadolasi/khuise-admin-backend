from django.db import models

# Create your models here.
class Produto_2(models.Model):



    nome = models.CharField(max_length=255)
    preço = models.FloatField()
    descrição = models.TextField()

    quantidade_de_p = models.IntegerField()
    quantidade_de_m = models.IntegerField()
    quantidade_de_g = models.IntegerField()


    imagem = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome



