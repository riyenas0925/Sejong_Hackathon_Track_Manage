# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Candidate',
            new_name='Track',
        ),
    ]
