# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ER_plotter', '0013_auto_20170328_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfuzz',
            name='clust_nb',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]