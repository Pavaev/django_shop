# Generated by Django 2.0.2 on 2018-03-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180322_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]