# Generated by Django 3.2.16 on 2022-11-26 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_storage_management', '0006_auto_20221126_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='dimension_width',
            field=models.FloatField(default=3),
        ),
    ]
