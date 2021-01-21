from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, ButtonHolder, Submit
from django import forms
from django.forms import inlineformset_factory

from apps.products import models, layouts


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'categories', 'price', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('price'),
                Field('categories'),
                Field('description'),
                Fieldset('Imagens', layouts.Formset('images_form')),
                Fieldset('Estoque', layouts.Formset('stock_form')),
                ButtonHolder(Submit('submit', 'Salvar')),
            )
        )


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.ProductImage
        fields = ('image',)


class StockForm(forms.ModelForm):
    class Meta:
        model = models.ProductStock
        fields = ('color', 'size', 'stock')


imagesFormSet = inlineformset_factory(
    models.Product,
    models.ProductImage,
    form=ImageForm,
    extra=1,
    can_delete=True,
)
stockFormSet = inlineformset_factory(
    models.Product,
    models.ProductStock,
    form=StockForm,
    extra=1,
    can_delete=True,
)
