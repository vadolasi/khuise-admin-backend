import graphene

from apps.accounts import mutations


class Mutation(graphene.ObjectType):
    create_invite = mutations.InviteCreateMutation.Field()

