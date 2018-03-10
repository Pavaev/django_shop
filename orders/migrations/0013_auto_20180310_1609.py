# Generated by Django 2.0.2 on 2018-03-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180226_0917'),
        ('orders', '0012_auto_20180310_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]