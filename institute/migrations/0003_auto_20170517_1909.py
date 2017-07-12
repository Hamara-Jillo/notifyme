# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_auto_20170517_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='logo',
            field=models.ForeignKey(to='images.UniversityLogo'),
        ),
    ]
