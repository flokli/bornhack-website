# Generated by Django 2.2.2 on 2019-06-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20180318_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountticket',
            name='token',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='shopticket',
            name='token',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sponsorticket',
            name='token',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
