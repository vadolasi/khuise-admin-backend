import graphene
from graphene_django_cud import mutations

from apps.products import models
from apps.products.types import *
from src.utils import base64_2image


class ProductCreateMutation(mutations.DjangoCreateMutation):
    class Meta:
        model = models.Product 


class ProductUpdateMutation(mutations.DjangoUpdateMutation):
    class Meta:
        model = models.Product
        optional_fields = ('name', 'description', 'price')


class ProductDeleteMutation(mutations.DjangoDeleteMutation):
    class Meta:
        model = models.Product


class StockBulkCreateMutation(mutations.DjangoBatchCreateMutation):
    class Meta:
        model = models.Stock


class StockUpdateMutation(mutations.DjangoUpdateMutation):
    class Meta:
        model = models.Stock
        exclude_fields = ('product',)


class StockDeleteMutation(mutations.DjangoDeleteMutation):
    class Meta:
        model = models.Stock


class ImageCreateMutation(mutations.DjangoCreateMutation):
    class Meta:
        model = models.Image

        field_types = {
            "image": graphene.String(required=True)
        }

    @classmethod
    def before_mutate(cls, root, info, input):
        input = type(input)(
            {
                'image': base64_2image(input['image']),
                'product': input['product']
            }
        )

        return input


class ImageBulkCreateMutation(mutations.DjangoBatchCreateMutation):
    class Meta:
        model = models.Image

        field_types = {
            "image": graphene.String(required=True)
        }

    @classmethod
    def before_mutate(cls, root, info, input):
        input = [
                type(input[0])({
                'image': base64_2image(image['image']),
                'product': image['product']
            }) for image in input
        ]

        return input


class ImageUpdateMutation(mutations.DjangoUpdateMutation):
    class Meta:
        model = models.Image

        field_types = {
            "image": graphene.String(required=True)
        }

    @classmethod
    def before_mutate(cls, root, info, input):
        input = type(input)(
            {
                'image': base64_2image(input['image'], exists=True),
                'product': input['product']
            }
        )
 
        return input

 
class ImageDeleteMutation(mutations.DjangoDeleteMutation):
    class Meta:
        model = models.Image
