# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-25 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20170711_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='public_credit_name',
            field=models.CharField(blank=True, help_text='The name you want to appear on in the credits section of the public website (on Team and People pages). Leave this empty if you want your name hidden on the public webpages.', max_length=100),
        ),
    ]
