from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from math import ceil


class Calculator:
    attack = 0
    attack_percent = Decimal(0)
    defense = 0
    defense_percent = Decimal(0)
    hp = 0
    hp_percent = Decimal(0)
    add1 = 0
    add1_percent = Decimal(0)
    add2 = 0
    add2_percent = Decimal(0)
    add3 = 0
    add3_percent = Decimal(0)
    crit_rate = Decimal(0)
    crit_damage = Decimal(0)
    reaction = "Null"
    em_bonus = Decimal(0)
    arts = False
    dmg_bonus = Decimal(0)
    skill_bonus = Decimal(0)
    ed_bonus = Decimal(0)
    resist = 10
    reduce = 0
    char_lvl = 90
    enemy_lvl = 90
    def_reduce = 0

    def print_stats(self) -> None:
        print("Attack:", self.attack, "| Attack Scaling:", self.attack_percent)
        print("Defense:", self.defense, "| Defense Scaling:", self.defense_percent)
        print("HP:", self.hp, "| HP Scaling:", self.hp_percent)

    @property
    def total_points(self) -> Decimal:
        self.print_stats()
        points = Decimal(0)
        points += self.attack * self.attack_percent / Decimal(100)
        points += self.defense * self.defense_percent / Decimal(100)
        points += self.hp * self.hp_percent / Decimal(100)
        points += self.add1 * self.add1_percent / Decimal(100)
        points += self.add2 * self.add2_percent / Decimal(100)
        points += self.add3 * self.add3_percent / Decimal(100)
        print("Points:", points)
        return points

    @property
    def total_bonuses_without_crit(self):
        bonus = Decimal(1)
        print("1", bonus)
        if self.reaction == "Reversed":
            bonus *= Decimal(1.5)
        elif self.reaction == "Full":
            bonus *= Decimal(2)
        if self.reaction != "Null" and self.reaction:
            if self.arts:
                bonus *= (Decimal(100) + self.em_bonus + 15) / 100
            else:
                bonus *= (Decimal(100) + self.em_bonus) / 100
        print("2", bonus)

        bonus *= (Decimal(100) + self.dmg_bonus + self.skill_bonus + self.ed_bonus) / 100
        print("3", (Decimal(100) + self.dmg_bonus + self.skill_bonus + self.ed_bonus) / 100)
        if self.resist - self.reduce >= 0:
            bonus *= Decimal(1) - Decimal((self.resist - self.reduce) / 100)
        else:
            bonus *= Decimal(1) + Decimal((self.reduce - self.resist) / 200)
        print("4", Decimal(1) + Decimal((self.resist - self.reduce) / 200))
        bonus *= (Decimal(100) + self.char_lvl) / (
                Decimal(100) + self.char_lvl
                + (Decimal(100) + self.enemy_lvl)
                * (Decimal(100) - self.def_reduce) / Decimal(100)
        )
        print("Total Bonus:", bonus)
        return bonus

    @property
    def total_damage(self):

        hit = self.total_points * self.total_bonuses_without_crit

        crit = hit * ((self.crit_damage + 100) / 100)
        average = ((self.crit_rate / 100) * (self.crit_damage / 100) + 1) * hit

        return {
            "hit": ceil(hit),
            "average": ceil(average),
            "crit": ceil(crit),
        }


class StatModel(models.Model, Calculator):
    name = models.CharField(max_length=80, default="Template")
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    attack = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    attack_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    defense = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    defense_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    hp = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    hp_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )

    add1 = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    add1_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    add2 = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    add2_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    add3 = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    add3_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )

    crit_rate = models.DecimalField(
        max_digits=3, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    crit_damage = models.DecimalField(
        max_digits=4, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(999.9)]
    )
    reaction = models.CharField(max_length=20, blank=True, null=True)

    em_bonus = models.DecimalField(
        max_digits=4, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(999.9)]
    )
    arts = models.BooleanField(default=False)
    dmg_bonus = models.DecimalField(
        max_digits=4, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(999.9)]
    )
    skill_bonus = models.DecimalField(
        max_digits=4, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(999.9)]
    )
    ed_bonus = models.DecimalField(
        max_digits=4, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(999.9)]
    )

    resist = models.IntegerField(
        default=10, validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    reduce = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(999)]
    )

    char_lvl = models.IntegerField(
        default=90, validators=[MinValueValidator(1), MaxValueValidator(90)]
    )
    enemy_lvl = models.IntegerField(
        default=90, validators=[MinValueValidator(1), MaxValueValidator(200)]
    )
    def_reduce = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
