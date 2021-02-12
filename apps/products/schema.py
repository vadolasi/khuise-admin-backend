import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from apps.products import types, mutations


class Query(graphene.ObjectType):
    product = relay.Node.Field(types.ProductNode)
    products = DjangoFilterConnectionField(types.ProductNode)


class Mutation(graphene.ObjectType):
    add_product = mutations.ProductCreateMutation.Field()
    update_product = mutations.ProductUpdateMutation.Field()
    delete_product = mutations.ProductDeleteMutation.Field()

