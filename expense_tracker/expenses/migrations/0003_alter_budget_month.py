# Generated by Django 5.1.5 on 2025-03-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='month',
            field=models.CharField(max_length=7),
        ),
    ]
