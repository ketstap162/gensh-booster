from numpy import float64

from django.shortcuts import render, redirect

from Estimation.models import StatModel, Calculator


def extract_or_no_change(instance: StatModel, data: dict, attribute: str) -> None:
    if data.get(attribute):
        setattr(instance, attribute, float64(data[attribute]))


def estimation_view(request):
    if request.method == "GET":
        return render(request, "estimation/estimation.html")

    if request.method == "POST":
        data = request.POST

        if request.POST.get("action") == "save":
            stats = StatModel.objects.get_or_create(name=data.get("template_name"))
        else:
            stats = Calculator()

        # ATTACK
        extract_or_no_change(stats, data, "attack")
        extract_or_no_change(stats, data, "attack_percent")

        # DEFENSE
        extract_or_no_change(stats, data, "defense")
        extract_or_no_change(stats, data, "defense_percent")

        # HP
        extract_or_no_change(stats, data, "hp")
        extract_or_no_change(stats, data, "hp_percent")

        # Additional 1
        extract_or_no_change(stats, data, "add1")
        extract_or_no_change(stats, data, "add1_percent")

        # Additional 2
        extract_or_no_change(stats, data, "add2")
        extract_or_no_change(stats, data, "add2_percent")

        # Additional 3
        extract_or_no_change(stats, data, "add3")
        extract_or_no_change(stats, data, "add3_percent")

        # CRITICAL
        extract_or_no_change(stats, data, "crit_rate")
        extract_or_no_change(stats, data, "crit_damage")

        # REACTIONS
        extract_or_no_change(stats, data, "reaction")
        reaction = data.get("reaction")

        extract_or_no_change(stats, data, "em_bonus")

        # DMG BONUS
        extract_or_no_change(stats, data, "dmg_bonus")
        extract_or_no_change(stats, data, "skill_bonus")
        extract_or_no_change(stats, data, "ed_bonus")

        # RESIST BONUS
        extract_or_no_change(stats, data, "resist")
        extract_or_no_change(stats, data, "reduce")

        # DEF BONUS
        extract_or_no_change(stats, data, "char_lvl")
        extract_or_no_change(stats, data, "enemy_lvl")
        extract_or_no_change(stats, data, "def_reduce")

        result = stats.total_damage

        print(result)

        context = {
            "result": result,
            "stats": stats,
            "reaction": data.get("reaction", "Null"),
        }

        return render(request, "estimation/estimation.html", context=context)


def estimation_save(request):
    return redirect("Estimation:estimation_view", permanent=True, foo='bar', method='POST')


def template_view(request):
    pass
