from numpy import float64

from django.shortcuts import render

from Estimation.models import Result, StatModel


def estimation_view(request):
    if request.method == "GET":
        return render(request, "estimation/estimation.html")

    if request.method == "POST":
        data = request.POST
        result = Result()
        stats = StatModel()

        # ATTACK
        if data.get("attack"):
            stats.attack = float64(data.get("attack", 0))
        if data.get("attack_percent"):
            stats.attack_percent = float64(data.get("attack_percent", 0))

        # DEFENSE
        if data.get("defense"):
            stats.defense = float64(data.get("defense", 0))
        if data.get("defense_percent"):
            stats.defense_percent = float64(data.get("defense_percent", 0))

        # HP
        if data.get("hp"):
            stats.hp = float64(data.get("hp", 0))
        if data.get("hp_percent"):
            stats.hp_percent = float64(data.get("hp_percent", 0))

        # Additional 1
        if data.get("add1"):
            stats.add1 = float64(data.get("add1", 0))
        if data.get("add1_percent"):
            stats.add1_percent = float64(data.get("add1_percent", 0))

        # Additional 2
        if data.get("add2"):
            stats.add2 = float64(data.get("add2", 0))
        if data.get("add2_percent"):
            stats.add2_percent = float64(data.get("add2_percent", 0))

        # Additional 3
        if data.get("add3"):
            stats.add3 = float64(data.get("add3", 0))
        if data.get("add3_percent"):
            stats.add3_percent = float64(data.get("add3_percent", 0))

        # CRITICAL
        if data.get("crit_rate"):
            stats.crit_rate = float64(data.get("crit_rate"))
        if data.get("crit_damage"):
            stats.crit_damage = float64(data.get("crit_damage"))

        # REACTIONS
        if data.get("reaction"):
            reaction = data.get("reaction")
            if reaction == "Null":
                stats.reaction = float64(1)
            elif reaction == "Reversed":
                stats.reaction = float64(1.5)
            elif reaction == "Full":
                stats.reaction = float64(2)

        if data.get("em_bonus"):
            stats.em_bonus = float64(data.get("em_bonus"))

        # DMG BONUS
        if data.get("dmg_bonus"):
            stats.dmg_bonus = float64(data.get("dmg_bonus"))

        if data.get("skill_bonus"):
            stats.skill_bonus = float64(data.get("skill_bonus"))

        if data.get("ed_bonus"):
            stats.ed_bonus = float64(data.get("ed_bonus"))

        # RESIST BONUS
        if data.get("resist"):
            stats.resist = float64(data.get("resist"))

        if data.get("reduce"):
            stats.reduce = float64(data.get("reduce"))

        # DEF BONUS
        if data.get("char_lvl"):
            stats.char_lvl = float64(data.get("char_lvl"))
        if data.get("enemy_lvl"):
            stats.enemy_lvl = float64(data.get("enemy_lvl"))
        if data.get("def_reduce"):
            stats.def_reduce = float64(data.get("def_reduce"))

        total = stats.total_damage
        result.hit = total["hit"]
        result.average = total["average"]
        result.crit = total["crit"]
        context = {
            "result": result,
            "stats": stats,
            "reaction": data.get("reaction", "Null"),
        }
        return render(request, "estimation/estimation.html", context=context)
