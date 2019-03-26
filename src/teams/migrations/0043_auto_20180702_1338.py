# Generated by Django 2.0.4 on 2018-07-02 18:38

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0042_auto_20180413_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shift_range', django.contrib.postgres.fields.ranges.DateTimeRangeField()),
                ('people_required', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='team',
            name='shifts_enabled',
            field=models.BooleanField(default=False, help_text='Does this team have shifts? This enables defining shifts for this team.'),
        ),
        migrations.AddField(
            model_name='teamshift',
            name='team',
            field=models.ForeignKey(help_text='The team this shift belongs to', on_delete=django.db.models.deletion.PROTECT, related_name='shifts', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='teamshift',
            name='team_members',
            field=models.ManyToManyField(to='teams.TeamMember'),
        ),
    ]
