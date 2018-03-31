# Generated by Django 2.0.2 on 2018-03-23 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180321_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]