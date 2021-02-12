import graphene
from django.conf import settings
from graphql_auth import relay
from graphene_django.debug import DjangoDebug

from apps.products import schema as products_schema


class Mutation(products_schema.Mutation, graphene.ObjectType):
    register = relay.Register.Field()
    send_password_reset_email = relay.SendPasswordResetEmail.Field()
    password_reset = relay.PasswordReset.Field()
    password_change = relay.PasswordChange.Field()
    archive_account = relay.ArchiveAccount.Field()
    delete_account = relay.DeleteAccount.Field()
    update_account = relay.UpdateAccount.Field()
    token_auth = relay.ObtainJSONWebToken.Field()
    verify_token = relay.VerifyToken.Field()
    refresh_token = relay.RefreshToken.Field()
    revoke_token = relay.RevokeToken.Field()


class Query(products_schema.Query, graphene.ObjectType):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(query=Query, mutation=Mutation)

