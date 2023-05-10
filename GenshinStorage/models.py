import os

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def char_big_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = "_".join(instance.full_name.split()).lower() + "_big" + extension

    return os.path.join("uploads/chars/", filename)


def char_small_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = "_".join(instance.full_name.split()).lower() + "_small" + extension

    return os.path.join("uploads/chars/", filename)


def element_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = instance.name.lower() + extension

    return os.path.join("uploads/elements/", filename)


def weapon_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = instance.name.lower() + extension

    return os.path.join("uploads/weapons/", filename)


def location_light_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = instance.name.lower() + "_light" + extension

    return os.path.join("uploads/locations/", filename)


def location_dark_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = instance.name.lower() + "_dark" + extension

    return os.path.join("uploads/locations/", filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Element(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to=element_image_file_path)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to=weapon_image_file_path)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    icon_light = models.ImageField(null=True, blank=True, upload_to=location_light_image_file_path)
    icon_dark = models.ImageField(null=True, blank=True, upload_to=location_dark_image_file_path)

    def __str__(self):
        return self.name


class Character(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    rarity = models.IntegerField(null=True)
    element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True)
    weapon = models.ForeignKey(Weapon, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    big_image = models.ImageField(null=True, blank=True, upload_to=char_big_image_file_path)
    small_image = models.ImageField(null=True, blank=True, upload_to=char_small_image_file_path)

    def __str__(self):
        return self.full_name

    def snake_name(self):
        return "_".join(self.full_name.split()).lower()

    def html_link(self):
        return "includes/heroes_details/" + self.snake_name() + ".html"


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

    def __str__(self):
        return f"{self.character}: {self.skill}"


class SkillData(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(13)])
    value = models.FloatField()
