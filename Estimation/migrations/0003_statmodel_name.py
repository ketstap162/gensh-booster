# Generated by Django 4.1.7 on 2023-05-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Estimation", "0002_delete_testmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="statmodel",
            name="name",
            field=models.CharField(default="Template", max_length=80),
        ),
    ]