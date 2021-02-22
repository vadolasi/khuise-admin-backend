from graphene_django_cud import DjangoCreateMutation as CreateMutation

from apps.accounts import models
from apps.accounts.types import *


class InviteCreateMutation(CreateMutation):
    class Meta:
        model = models.Invite

