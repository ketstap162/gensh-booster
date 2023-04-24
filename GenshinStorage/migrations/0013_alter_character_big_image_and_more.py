# Generated by Django 4.1.7 on 2023-04-24 17:13

import GenshinStorage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GenshinStorage", "0012_character_element"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="big_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=GenshinStorage.models.char_big_image_file_path,
            ),
        ),
        migrations.AlterField(
            model_name="character",
            name="small_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=GenshinStorage.models.char_small_image_file_path,
            ),
        ),
    ]
