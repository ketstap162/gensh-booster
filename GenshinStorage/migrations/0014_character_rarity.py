# Generated by Django 4.1.7 on 2023-04-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GenshinStorage", "0013_alter_character_big_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="rarity",
            field=models.IntegerField(null=True),
        ),
    ]