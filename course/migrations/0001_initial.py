# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('units', models.IntegerField(default=3)),
                ('description', models.TextField(max_length=500)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('choice', models.CharField(max_length=50, choices=[(b'C', b'COMPULSORY'), (b'E', b'ELECTIVE')])),
                ('programme', models.ForeignKey(related_name='courses', to='programme.Programme')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('programme', 'title')]),
        ),
    ]
