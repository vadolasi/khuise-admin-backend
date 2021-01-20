import graphene
from graphene_django import DjangoObjectType

from apps.products import models


class ListTypeNode(DjangoObjectType):
    class Meta:
        model = models.Product
        filter_fields = ['name', 'description', 'categories', 'stock']
        interfaces = [graphene.relay.Node]
