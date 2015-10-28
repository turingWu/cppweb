# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supperuser',
            options={'verbose_name_plural': '\u56e2\u961f\u6210\u5458'},
        ),
        migrations.AlterField(
            model_name='team',
            name='achievement',
            field=models.ForeignKey(blank=True, to='webapp.Achievements', null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='prize',
            field=models.ForeignKey(related_name='teamPrize_set', blank=True, to='webapp.Prizes', null=True),
        ),
    ]
