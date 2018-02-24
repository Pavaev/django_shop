# Generated by Django 2.0.2 on 2018-02-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_productinorder_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='is_active',
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
