# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.IntegerField()),
                ('key', models.IntegerField()),
                ('answer', models.CharField(max_length=1)),
                ('content', models.TextField()),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(max_length=30)),
                ('p_name', models.CharField(max_length=100)),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('score3', models.IntegerField()),
                ('sum_score', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='participants',
            unique_together=set([('p_id', 'p_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='databank',
            unique_together=set([('q_id', 'key')]),
        ),
    ]
