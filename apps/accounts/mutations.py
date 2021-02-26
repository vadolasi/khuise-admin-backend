from graphene_django_cud import mutations

from apps.accounts import models
from apps.accounts.types import *
from src.tasks import send_email_from_template


class InviteCreateMutation(mutations.DjangoCreateMutation):
    class Meta:
        model = models.Invite

        auto_context_fields = {
            'by_user': 'user'
        }

    @classmethod
    def before_mutate(cls, root, info, input):
        send_email_from_template.delay(
            template_name='email/admin_invite',
            context={
                'code': self.code,
                'user': info.context.user
            },
            subject='Convite para a administração do e-commerce Khuise',
            recipient_list=[self.email],
        )

