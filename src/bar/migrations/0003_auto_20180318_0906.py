# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-18 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("bar", "0002_auto_20170916_2128")]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="products",
                to="bar.ProductCategory",
            ),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="camp",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="camps.Camp"
            ),
        ),
    ]
