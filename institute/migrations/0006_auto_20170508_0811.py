# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_auto_20170507_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='programme',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
