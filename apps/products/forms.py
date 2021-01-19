from django import forms

from apps.products import models


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'price', 'description', 'images')
