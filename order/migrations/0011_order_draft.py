# Generated by Django 3.1.4 on 2021-02-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_orderitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='draft',
            field=models.IntegerField(default=True, verbose_name='Draft'),
        ),
    ]
