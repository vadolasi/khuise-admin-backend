import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from apps.accounts import types, mutations


class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass

