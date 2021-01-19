import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from apps.products import schema


class Query(schema.Query, graphene.ObjectType):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(query=Query)
