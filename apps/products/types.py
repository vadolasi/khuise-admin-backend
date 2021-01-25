import graphene
from graphene_django import DjangoObjectType

from apps.products import models


class ProductNode(DjangoObjectType):
    class Meta:
        model = models.Product
        filter_fields = ['name', 'description', 'stocks', 'images']
        interfaces = [graphene.relay.Node]


class ProductImageNode(DjangoObjectType):
    class Meta:
        model = models.ProductImage
        filter_fields = ['product']
        interfaces = [graphene.relay.Node]
