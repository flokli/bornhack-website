# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-12 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0039_fix_irc_channels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='irc_channel',
        ),
        migrations.RemoveField(
            model_name='team',
            name='irc_channel_managed',
        ),
        migrations.RemoveField(
            model_name='team',
            name='irc_channel_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='irc_channel_private',
        ),
    ]
