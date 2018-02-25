# Generated by Django 2.0.2 on 2018-02-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=None, max_length=48),
        ),
    ]