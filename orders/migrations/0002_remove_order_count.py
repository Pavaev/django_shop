# Generated by Django 2.0.2 on 2018-03-14 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='count',
        ),
    ]