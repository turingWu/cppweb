# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address', models.CharField(max_length=30, null=True, blank=True)),
                ('unit', models.CharField(max_length=15, null=True, blank=True)),
                ('qq', models.PositiveIntegerField(null=True, verbose_name=b'qq\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('dec', models.CharField(max_length=100, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe4\xbf\xa1\xe6\x81\xaf', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe6\x88\x90\xe6\x9e\x9c\xe6\xa0\x87\xe9\xa2\x98')),
                ('dec', models.CharField(max_length=100, verbose_name=b'\xe6\x88\x90\xe6\x9e\x9c\xe8\xaf\xa6\xe7\xbb\x86\xe4\xbb\x8b\xe7\xbb\x8d')),
            ],
        ),
        migrations.CreateModel(
            name='Fans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prizes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matchName', models.CharField(max_length=20, verbose_name=b'\xe8\xb5\x9b\xe5\x90\x8d')),
                ('height', models.CharField(max_length=6, choices=[(b'one', b'\xe4\xb8\x96\xe7\x95\x8c\xe7\xba\xa7'), (b'two', b'\xe5\x9b\xbd\xe5\xae\xb6\xe7\xba\xa7'), (b'three', b'\xe7\x9c\x81\xe7\xba\xa7'), (b'four', b'\xe5\x8c\xba\xe7\xba\xa7'), (b'others', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('grade', models.CharField(max_length=6, choices=[(b'ONE', b'\xe4\xb8\x80\xe7\xad\x89\xe5\xa5\x96'), (b'TWO', b'\xe4\xba\x8c\xe7\xad\x89\xe5\xa5\x96'), (b'THREE', b'\xe4\xb8\x89\xe7\xad\x89\xe5\xa5\x96'), (b'FOUR', b'\xe7\x89\xb9\xe7\xad\x89\xe5\xa5\x96'), (b'OTHERS', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('dec', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('abouts', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x9b\xa2\xe9\x98\x9f\xe4\xbb\x8b\xe7\xbb\x8d', blank=True)),
                ('achievement', models.ForeignKey(to='webapp.Achievements')),
                ('prize', models.ForeignKey(related_name='teamPrize_set', to='webapp.Prizes')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=8000)),
                ('date_publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('text_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webapp.Text')),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe6\xa0\x87\xe9\xa2\x98')),
            ],
            bases=('webapp.text',),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('text_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webapp.Text')),
            ],
            bases=('webapp.text',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('text_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webapp.Text')),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe6\xa0\x87\xe9\xa2\x98')),
            ],
            bases=('webapp.text',),
        ),
        migrations.CreateModel(
            name='SupperUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('supperDec', models.CharField(max_length=500, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('team', models.ForeignKey(to='webapp.Team')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('webapp.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('text_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webapp.Text')),
                ('title', models.CharField(max_length=100)),
            ],
            bases=('webapp.text',),
        ),
        migrations.AddField(
            model_name='fans',
            name='user',
            field=models.ForeignKey(related_name='care_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='tweets',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fans',
            name='god',
            field=models.ForeignKey(related_name='fans_set', to='webapp.SupperUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='to',
            field=models.ForeignKey(related_name='beComment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(to='webapp.SupperUser'),
        ),
    ]
