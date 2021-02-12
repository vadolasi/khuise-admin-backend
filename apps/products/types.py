import graphene
from graphene.types import generic
from graphene_django import DjangoObjectType

from apps.products import models


class ProductNode(DjangoObjectType):
    class Meta:
        model = models.Product
        filter_fields = ['name', 'description', 'realese_date', 'stock', 'images']
        interfaces = [graphene.relay.Node]

    pk = graphene.Int()

    def resolve_pk(self, info):
        return self.pk


class CategoryNode(DjangoObjectType):
    class Meta:
        model = models.Category
        filter_fields = ['name']
        interfaces = [graphene.relay.Node]

    pk = graphene.Int()

    def resolve_pk(self, info):
        return self.pk


class ImageNode(DjangoObjectType):
    class Meta:
        model = models.Image
        filter_fields = ['product']
        interfaces = [graphene.relay.Node]

    pk = graphene.Int()

    def resolve_pk(self, info):
        return self.pk


class StockNode(DjangoObjectType):
    class Meta:
        model = models.Stock
        filter_fields = ['product']
        interfaces = [graphene.relay.Node]

    pk = graphene.Int()

    def resolve_pk(self, info):
        return self.pk

