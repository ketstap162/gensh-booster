# Generated by Django 4.1.7 on 2023-04-24 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("GenshinStorage", "0015_location_weapon_remove_character_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="GenshinStorage.location",
            ),
        ),
        migrations.AddField(
            model_name="character",
            name="weapon",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="GenshinStorage.weapon",
            ),
        ),
    ]