# Generated by Django 3.2.16 on 2022-11-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_storage_management', '0011_client_is_reporting_as_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='unit_access',
            field=models.ManyToManyField(default=None, related_name='units', to='self_storage_management.Unit'),
        ),
    ]
