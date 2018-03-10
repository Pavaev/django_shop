# Generated by Django 2.0.2 on 2018-03-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20180228_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productinbasket',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ProductInBasket',
        ),
        migrations.DeleteModel(
            name='ProductInOrder',
        ),
    ]
