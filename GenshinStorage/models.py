from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()


class Character(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    element = models.CharField(max_length=40)
    weapon = models.CharField(max_length=255)
    description = models.TextField()


class Skill(models.Model):
    NORMAL_ATTACK = "NA"
    HOLD_ATTACK = "HA"
    ELEMENTARY_SKILL = "E"
    ELEMENTARY_BURST = "ULT"
    ATTACK_CHOICES = [
        (NORMAL_ATTACK, "Normal Attack"),
        (HOLD_ATTACK, "Hold Attack"),
        (ELEMENTARY_SKILL, "Elementary Skill"),
        (ELEMENTARY_BURST, "Elementary Burst")
    ]
    skill = models.CharField(
        max_length=5,
        choices=ATTACK_CHOICES,
    )
    character = models.ForeignKey(Character, on_delete=models.CASCADE)


class SkillData(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(13)])
    value = models.FloatField()
