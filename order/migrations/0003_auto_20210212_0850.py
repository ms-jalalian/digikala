# Generated by Django 3.1.4 on 2021-02-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210212_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitems',
            name='order',
        ),
        migrations.AddField(
            model_name='basketitems',
            name='basket',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.basket', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='basketitems',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='quantity'),
        ),
    ]
