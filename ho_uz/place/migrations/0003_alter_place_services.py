# Generated by Django 4.2.13 on 2024-07-05 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_services_place_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='services',
            field=models.ManyToManyField(blank=True, to='place.services'),
        ),
    ]