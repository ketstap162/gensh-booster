from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from numpy import float64
from django.db import models
from math import ceil


class Calculator:
    attack = float64(0)
    attack_percent = float64(0)
    defense = float64(0)
    defense_percent = float64(0)
    hp = float64(0)
    hp_percent = float64(0)
    add1 = float64(0)
    add1_percent = float64(0)
    add2 = float64(0)
    add2_percent = float64(0)
    add3 = float64(0)
    add3_percent = float64(0)
    crit_rate = float64(0)
    crit_damage = float64(0)
    reaction = "Null"
    em_bonus = float64(0)
    arts = False
    dmg_bonus = float64(0)
    skill_bonus = float64(0)
    ed_bonus = float64(0)
    resist = float64(10)
    reduce = float64(0)
    char_lvl = float64(90)
    enemy_lvl = float64(90)
    def_reduce = float64(0)

    def print_stats(self) -> None:
        print("Attack:", self.attack, "| Attack Scaling:", self.attack_percent)
        print("Defense:", self.defense, "| Defense Scaling:", self.defense_percent)
        print("HP:", self.hp, "| HP Scaling:", self.hp_percent)

    @property
    def total_points(self):
        self.print_stats()
        points = float64(0)
        points += self.attack * self.attack_percent / float64(100)
        points += self.defense * self.defense_percent / float64(100)
        points += self.hp * self.hp_percent / float64(100)
        points += self.add1 * self.add1_percent / float64(100)
        points += self.add2 * self.add2_percent / float64(100)
        points += self.add3 * self.add3_percent / float64(100)
        print("Points:", points)
        return points

    @property
    def total_bonuses_without_crit(self):
        bonus = float64(1)
        print("1", bonus)
        if self.reaction == "Reversed":
            bonus *= float64(1.5)
        elif self.reaction == "Full":
            bonus *= float64(2)
        if self.reaction != "Null" and self.reaction:
            if self.arts:
                bonus *= (float64(100) + self.em_bonus + 15) / 100
            else:
                bonus *= (float64(100) + self.em_bonus) / 100
        print("2", bonus)

        bonus *= (float64(100) + self.dmg_bonus + self.skill_bonus + self.ed_bonus) / 100
        print("3", (float64(100) + self.dmg_bonus + self.skill_bonus + self.ed_bonus) / 100)
        if self.resist - self.reduce >= 0:
            bonus *= float64(1) - ((self.resist - self.reduce) / 100)
        else:
            bonus *= float64(1) + ((self.reduce - self.resist) / 200)
        print("4", float64(1) + ((self.resist - self.reduce) / 200))
        bonus *= (float64(100) + self.char_lvl) / (
                float64(100) + self.char_lvl
                + (float64(100) + self.enemy_lvl)
                * (float64(100) - self.def_reduce) / float64(100)
        )
        print("Total Bonus:", bonus)
        return bonus

    @property
    def total_damage(self):

        hit = self.total_points * self.total_bonuses_without_crit

        crit = hit * ((self.crit_damage + 100) / 100)
        average = ((self.crit_rate / 100) * (self.crit_damage / 100) + 100) / 100 * hit

        return {
            "hit": ceil(hit),
            "average": ceil(average),
            "crit": ceil(crit),
        }


class StatModel(models.Model, Calculator):
    name = models.CharField(max_length=80, default="Template")
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    attack = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    attack_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    defense = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    defense_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    hp = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    hp_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )

    add1 = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    add1_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    add2 = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    add2_percent = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999.99)]
    )
    add3 = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
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

    resist = models.DecimalField(
        max_digits=3, decimal_places=0, default=10, validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    reduce = models.DecimalField(
        max_digits=3, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(999)]
    )

    char_lvl = models.DecimalField(
        max_digits=3, decimal_places=0, default=90, validators=[MinValueValidator(1), MaxValueValidator(90)]
    )
    enemy_lvl = models.DecimalField(
        max_digits=3, decimal_places=0, default=90, validators=[MinValueValidator(1), MaxValueValidator(200)]
    )
    def_reduce = models.DecimalField(
        max_digits=3, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
