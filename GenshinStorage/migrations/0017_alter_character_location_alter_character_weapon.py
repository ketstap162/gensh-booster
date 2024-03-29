# Generated by Django 4.1.7 on 2023-04-24 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("GenshinStorage", "0016_character_location_character_weapon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="GenshinStorage.location",
            ),
        ),
        migrations.AlterField(
            model_name="character",
            name="weapon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="GenshinStorage.weapon",
            ),
        ),
    ]
