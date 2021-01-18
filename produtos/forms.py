from django import forms

from .models import Produto_2

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto_2
        fields = ('nome', 'preço', 'quantidade_de_p', 'quantidade_de_m', 'quantidade_de_g', 'descrição', 'imagem', )