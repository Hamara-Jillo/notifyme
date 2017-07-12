# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_institute_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='url',
        ),
    ]
