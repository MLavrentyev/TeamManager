# Generated by Django 2.1.3 on 2019-01-09 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseRequests', '0010_auto_20190107_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='shipping_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]