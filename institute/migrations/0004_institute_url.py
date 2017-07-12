# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20170517_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='url',
            field=models.URLField(default=datetime.datetime(2017, 5, 21, 21, 0, 28, 202178, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
