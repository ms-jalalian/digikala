# Generated by Django 3.1.4 on 2021-01-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='Detail'),
        ),
    ]
