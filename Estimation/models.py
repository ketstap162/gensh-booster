from numpy import float64


class StatModel:
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
    reaction = float64(1)

    em_bonus = float64(0)
    dmg_bonus = float64(0)
    skill_bonus = float64(0)
    ed_bonus = float64(0)

    resist = float64(0)
    reduce = float64(0)

    char_lvl = float64(0)
    enemy_lvl = float64(0)
    def_reduce = float64(0)

    @property
    def total_points(self):
        atk = float64(self.attack) * float64(self.attack_percent)
        defence = float64(self.defence) * float64(self.defence_percent)
        hp = float64(self.hp) * float64(self.hp_percent)
        add1 = float64(self.add1) * float64(self.add1_percent)
        add2 = float64(self.add2) * float64(self.add2_percent)
        add3 = float64(self.add3) * float64(self.add3_percent)

        return atk + defence + hp + add1 + add2 + add3

    @property
    def total_bonuses_without_crit(self):
        bonus = float64(1)
        bonus *= self.reaction
        bonus *= self.em_bonus / 100
        bonus *= (float64(100) + self.dmg_bonus + self.skill_bonus + self.ed_bonus) / 100
        if self.resist - self.reduce < 0:
            bonus *= float64(-1) * self.resist - self.reduce
        else:
            bonus *= float64(1) - (self.resist - self.reduce)
        bonus *= self.resist
        bonus *= self.ed_bonus
        return bonus

    @property
    def total_damage(self):

        hit = self.total_bonuses_without_crit * self.total_points

        crit = hit * (self.crit_damage + 100) / 100
        average = (self.crit_rate * self.crit_damage + 100) / 100 * hit
        return {
            "hit": hit,
            "average": average,
            "crit": crit,
        }


class Result:
    hit = None
    crit = None
    average = None
