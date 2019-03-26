# Generated by Django 2.0.4 on 2018-05-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0051_auto_20180512_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventproposal',
            name='allow_video_recording',
            field=models.BooleanField(default=False, help_text='Check if we can video record the event. Leave unchecked to avoid video recording.'),
        ),
    ]
