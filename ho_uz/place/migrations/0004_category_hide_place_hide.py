# Generated by Django 4.2.13 on 2024-07-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_alter_place_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть?'),
        ),
        migrations.AddField(
            model_name='place',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть?'),
        ),
    ]