# Generated by Django 5.1.5 on 2025-01-23 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heart_rate',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)]),
        ),
    ]