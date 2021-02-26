# Generated by Django 3.0.5 on 2021-02-22 11:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='endereço de email')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='código')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='data do envio')),
            ],
            options={
                'verbose_name': 'Convite',
                'verbose_name_plural': 'Convites',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='endereço de email')),
                ('first_name', models.CharField(max_length=128, verbose_name='primeiro nome')),
                ('last_name', models.CharField(max_length=128, verbose_name='sobrenome')),
                ('is_staff', models.BooleanField(default=False, verbose_name='é membro da equipe')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='é superusuário')),
                ('is_active', models.BooleanField(default=True, verbose_name='é ativo')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='último login')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='data de registro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
