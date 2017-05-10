# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_programme_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='duration',
            field=models.IntegerField(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7')]),
        ),
    ]
