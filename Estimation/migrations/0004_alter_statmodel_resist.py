# Generated by Django 4.1.7 on 2023-05-13 18:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Estimation", "0003_statmodel_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statmodel",
            name="resist",
            field=models.DecimalField(
                decimal_places=0,
                default=10,
                max_digits=3,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999),
                ],
            ),
        ),
    ]
