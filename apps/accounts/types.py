import graphene
from graphene.types import generic
from graphene_django import DjangoObjectType

from apps.accounts import models


class InviteNode(DjangoObjectType):
    class Meta:
        model = models.Invite
        interfaces = [graphene.relay.Node]

