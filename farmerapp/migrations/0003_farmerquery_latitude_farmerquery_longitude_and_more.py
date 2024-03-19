# Generated by Django 5.0.1 on 2024-01-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0002_farmerquery'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerquery',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farmerquery',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farmerquery',
            name='weather_condition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]