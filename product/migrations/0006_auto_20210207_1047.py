# Generated by Django 3.1.4 on 2021-02-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210204_1158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
    ]