# Generated by Django 4.1.7 on 2023-05-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Estimation", "0006_alter_statmodel_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="statmodel",
            name="arts",
            field=models.BooleanField(default=False),
        ),
    ]
