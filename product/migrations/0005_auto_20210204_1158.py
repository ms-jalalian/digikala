# Generated by Django 3.1.4 on 2021-02-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210204_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
    ]
