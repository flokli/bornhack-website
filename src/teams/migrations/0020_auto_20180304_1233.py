# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-04 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("teams", "0019_auto_20180304_1019")]

    operations = [
        migrations.AlterField(
            model_name="teamarea",
            name="camp",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="teamareas",
                to="camps.Camp",
            ),
        )
    ]
