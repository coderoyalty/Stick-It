# Generated by Django 3.1.2 on 2020-10-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_auto_20201023_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
    ]