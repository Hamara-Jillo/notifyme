# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='universitylogo',
            name='name',
            field=models.CharField(default=datetime.datetime(2017, 5, 17, 19, 33, 14, 419150, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
