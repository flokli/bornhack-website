# Generated by Django 2.1.7 on 2019-07-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0006_auto_20190713_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='author',
            field=models.CharField(default='Unnamed', help_text='Let people know who posted this', max_length=100),
        ),
    ]
