# Generated by Django 3.1.4 on 2021-02-12 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20210212_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='basket_items', related_query_name='basket_items', to='order.basket', verbose_name='Basket'),
        ),
    ]
