from graphene_django_cud import DjangoCreateMutation as CreateMutation
from graphene_django_cud import DjangoUpdateMutation as UpdateMutation
from graphene_django_cud import DjangoDeleteMutation as DeleteMutation
from graphene_djnago_cud import DjangoBatchCreateMutation as BulkCreateMutation
from graphene_django_cud import DjangoBatchUpdateMutation as BulkUpdateMutation
from graphene_django_cud import DjangoBatchDeleteMutation as BulkDeleteMutation
from graphene_file_upload.scalars import Upload

from apps.products import models
from apps.products.types import *


class ProductCreateMutation(CreateMutation):
    class Meta:
        model = models.Product


class ProductUpdateMutation(UpdateMutation):
    class Meta:
        model = models.Product


class ProductDeleteMutation(DeleteMutation):
    class Meta:
        model = models.Product


class StockBulkCreateMutation(BulkCreateMutation):
    class Meta:
        model = models.Stock


class StockUpdateMutation(UpdateMutation):
    class Meta:
        model = models.Stock


class StockDeleteMutation(DeleteMutation):
    class Meta:
        model = models.Stock


class ImageBulkCreateMutation(BulkCreateMutation):
    class Meta:
        model = models.Image

        field_types = {
            "image": Upload(required=True)
        }

    @classmethod
    def handle_image(cls, value, *args, **kwargs):
        return value[0]


class ImageUpdateMutation(UpdateMutation):
    class Meta:
        model = models.Image

        field_types = {
            "image": Upload(required=True)
        }

    @classmethod
    def handle_image(cls, value, *args, **kwargs):
        return value[0]


class ImageDeleteMutation(DeleteMutation):
    class Meta:
        model = models.Image

