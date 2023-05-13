from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from numpy import float64
from django.db import models


class Calculator:
    attack = float64(0)
    attack_percent = float64(0)
    defence = float64(0)
    defence_percent = float64(0)
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
    dmg_bonus = float64(0)
    skill_bonus = float64(0)
    ed_bonus = float64(0)
    resist = float64(10)
    reduce = float64(0)
    char_lvl = float64(90)
    enemy_lvl = float64(200)
    def_reduce = float64(0)

    def print_stats(self) -> None:
        print("Attack:", self.attack)
        print("Attack Scaling:", self.attack_percent)

    @property
    def total_points(self):
        atk = self.attack * self.attack_percent / 100
        defence = self.defence * self.defence_percent / 100
        hp = self.hp * self.hp_percent / 100
        add1 = self.add1 * self.add1_percent / 100
        add2 = self.add2 * self.add2_percent / 100
        add3 = self.add3 * self.add3_percent / 100

        print("Total Points:", atk + defence + hp + add1 + add2 + add3)
        return atk + defence + hp + add1 + add2 + add3

    @property
    def total_bonuses_without_crit(self):
        bonus = float64(1)
        print("1", bonus)
        bonus *= self.reaction
        print("2", bonus)
        bonus *= (float64(100) + self.em_bonus) / 100
        print("3", bonus)
        bonus *= (float64(100) + self.dmg_bonus + self.skill_bonus + self.ed_bonus) / 100
        print("4", bonus)
        if self.resist - self.reduce >= 0:
            bonus *= float64(1) - ((self.resist - self.reduce) / 100)
        else:
            bonus *= float64(1) + ((self.resist - self.reduce) / 200)
        print("5", bonus)
        bonus *= self.resist
        print("6", bonus)
        bonus *= (float64(100) + self.ed_bonus) / 100

        print("Total Bonus:", bonus)
        return bonus

    @property
    def total_damage(self):

        hit = self.total_points * self.total_bonuses_without_crit

        crit = hit * ((self.crit_damage + 100) / 100)
        average = ((self.crit_rate / 100) * (self.crit_damage / 100) + 100) / 100 * hit

        return {
            "hit": hit,
            "average": average,
            "crit": crit,
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
    defence = models.DecimalField(
        max_digits=5, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
    defence_percent = models.DecimalField(
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
    reaction = models.DecimalField(
        max_digits=2, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(2)]
    )

    em_bonus = models.DecimalField(
        max_digits=4, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(999.9)]
    )
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
