# Generated by Django 2.0.5 on 2018-05-31 15:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseRequests', '0002_auto_20180531_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='cost_currency',
        ),
        migrations.AlterField(
            model_name='request',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
