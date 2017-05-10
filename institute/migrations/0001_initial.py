# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
                ('year', models.IntegerField(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7')])),
                ('semester', models.IntegerField(choices=[(b'1', b'1'), (b'2', b'2')])),
                ('choice', models.CharField(max_length=50, choices=[(b'C', b'COMPULSORY'), (b'E', b'ELECTIVE')])),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('logo', models.ImageField(upload_to=b'media/instituteLogo/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('title', models.CharField(max_length=128, choices=[(b'Bridging', b'Bridging'), (b'Diploma', b'Diploma'), (b'Degree', b'Degree'), (b'Masters', b'Masters'), (b'Doctorate', b'Doctorate')])),
                ('department', models.ForeignKey(related_name='programmes', to='institute.Department')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('institute', models.ForeignKey(related_name='schools', to='institute.Institute')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(related_name='departments', to='institute.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='programme',
            field=models.ForeignKey(related_name='courses', to='institute.Programme'),
        ),
        migrations.AlterUniqueTogether(
            name='school',
            unique_together=set([('institute', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='programme',
            unique_together=set([('department', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together=set([('school', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('programme', 'title')]),
        ),
    ]
