import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from apps.products import types


class Query(graphene.ObjectType):
    product = relay.Node.Field(types.ListTypeNode)
    products = DjangoFilterConnectionField(types.ListTypeNode)
