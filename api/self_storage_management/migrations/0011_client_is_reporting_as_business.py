# Generated by Django 3.2.16 on 2022-11-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_storage_management', '0010_auto_20221126_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_reporting_as_business',
            field=models.BooleanField(default=False),
        ),
    ]