# Generated by Django 4.1.7 on 2023-04-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GenshinStorage", "0004_skill_skilldata_delete_characterdata"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="weapon",
            field=models.CharField(default="Claymore", max_length=255),
            preserve_default=False,
        ),
    ]
