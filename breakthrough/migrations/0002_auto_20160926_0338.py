# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-26 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breakthrough', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Participant',
        ),
    ]