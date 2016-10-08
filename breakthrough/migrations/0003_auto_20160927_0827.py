# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-27 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakthrough', '0002_auto_20160926_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='p_alive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='p_class',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='participant',
            name='p_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='p_key',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='participant',
            name='score1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='score2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='score3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='sum_score',
            field=models.IntegerField(default=0),
        ),
    ]
