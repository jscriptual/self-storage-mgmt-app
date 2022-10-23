# Generated by Django 3.2.16 on 2022-10-22 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('self_storage_management', '0002_auto_20221015_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('unit_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='self_storage_management.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('business_name', models.TextField(blank=True)),
                ('email_address', models.TextField(blank=True)),
                ('phone_number', models.TextField(blank=True)),
                ('street_address', models.TextField(blank=True)),
                ('unit_access', models.ManyToManyField(blank=True, related_name='customers', to='self_storage_management.Unit')),
            ],
        ),
    ]