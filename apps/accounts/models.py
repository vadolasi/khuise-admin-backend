import uuid

from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone

from src.tasks import send_email_from_template


class UserManager(BaseUserManager):
    def _create_user(
        self, email,
        first_name,
        last_name,
        password,
        is_staff,
        is_superuser,
        **extra_fields
    ):
        if not email:
            raise ValueError('Users must have an email address')
        elif not first_name or not last_name:
            raise ValueError(
                'Users must have an email first name and last name',
            )

        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(
        self,
        email,
        first_name,
        last_name,
        password,
        **extra_fields
    ):
        return self._create_user(
            email,
            first_name,
            last_name,
            password,
            False,
            False,
            **extra_fields
        )

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        password,
        **extra_fields
    ):
        user = self._create_user(
            email,
            first_name,
            last_name,
            password,
            True,
            True,
            **extra_fields
        )

        return user


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField('endereço de email', unique=True)
    first_name = models.CharField('primeiro nome', max_length=128)
    last_name = models.CharField('sobrenome', max_length=128)
    is_staff = models.BooleanField('é membro da equipe', default=False)
    is_superuser = models.BooleanField('é superusuário', default=False)
    is_active = models.BooleanField('é ativo', default=True)
    last_login = models.DateTimeField('último login', null=True, blank=True)
    date_joined = models.DateTimeField('data de registro', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Invite(models.Model):
    email = models.EmailField('endereço de email')
    code = models.UUIDField('código', default=uuid.uuid4, editable=False)
    send_date = models.DateTimeField('data do envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Convite'
        verbose_name_plural = 'Convites'

    def __str__(self):
        return f'Enviado para {self.email} em {self.sent_date}'

    def save(self):
        send_email_from_template.delay(
            template_name='email/admin_invite',
            context={
                'code': self.code
            },
            subject='Convite para a administração do e-commerce Khuise',
            recipient_list=[self.email],
        )
        super(Invite, self).save(*args, **kwargs)

