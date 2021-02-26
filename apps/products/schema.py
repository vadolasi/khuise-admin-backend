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
    add_stock = mutations.StockBulkCreateMutation.Field()
    update_stock = mutations.StockUpdateMutation.Field()
    delete_stock = mutations.StockDeleteMutation.Field()
    add_image = mutations.ImageCreateMutation.Field()
    add_images = mutations.ImageBulkCreateMutation.Field()
    update_image = mutations.ImageUpdateMutation.Field()
    delete_image = mutations.ImageDeleteMutation.Field()
