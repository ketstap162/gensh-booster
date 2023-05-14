from datetime import datetime
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from numpy import float64

from django.shortcuts import render, redirect

from Estimation.models import StatModel, Calculator


def extract_or_no_change(instance: StatModel, data: dict, attribute: str, data_type: type = str) -> None:
    if data_type is str:
        setattr(instance, attribute, data[attribute])
    else:
        if data.get(attribute):
            if data.get(attribute):
                try:
                    setattr(instance, attribute, data_type(data[attribute]))
                except ValueError:
                    setattr(instance, attribute, data[attribute])


def full_data_extract(instance: StatModel | Calculator, data: dict) -> None:
    # ATTACK
    extract_or_no_change(instance, data, "attack", int)
    extract_or_no_change(instance, data, "attack_percent", Decimal)

    # DEFENSE
    extract_or_no_change(instance, data, "defense", int)
    extract_or_no_change(instance, data, "defense_percent", Decimal)

    # HP
    extract_or_no_change(instance, data, "hp", int)
    extract_or_no_change(instance, data, "hp_percent", Decimal)

    # Additional 1
    extract_or_no_change(instance, data, "add1", int)
    extract_or_no_change(instance, data, "add1_percent", Decimal)

    # Additional 2
    extract_or_no_change(instance, data, "add2", int)
    extract_or_no_change(instance, data, "add2_percent", Decimal)

    # Additional 3
    extract_or_no_change(instance, data, "add3", int)
    extract_or_no_change(instance, data, "add3_percent", Decimal)

    # CRITICAL
    extract_or_no_change(instance, data, "crit_rate", Decimal)
    extract_or_no_change(instance, data, "crit_damage", Decimal)

    # REACTIONS
    extract_or_no_change(instance, data, "reaction")
    extract_or_no_change(instance, data, "em_bonus", Decimal)
    extract_or_no_change(instance, data, "arts", Decimal)

    # DMG BONUS
    extract_or_no_change(instance, data, "dmg_bonus", Decimal)
    extract_or_no_change(instance, data, "skill_bonus", Decimal)
    extract_or_no_change(instance, data, "ed_bonus", Decimal)

    # RESIST BONUS
    extract_or_no_change(instance, data, "resist", int)
    extract_or_no_change(instance, data, "reduce", int)

    # DEF BONUS
    extract_or_no_change(instance, data, "char_lvl", int)
    extract_or_no_change(instance, data, "enemy_lvl", int)
    extract_or_no_change(instance, data, "def_reduce", int)


def estimation_view(request):
    print(request.GET)
    if request.method == "GET":
        if request.GET.get("stats_id"):
            stats_id = request.GET.get("stats_id")
            stats = StatModel.objects.get(pk=stats_id)

            if stats.user_id == request.user:
                context = {"stats": StatModel.objects.get(pk=stats_id)}
                return render(request, "estimation/estimation.html", context=context)
        return render(request, "estimation/estimation.html")

    if request.method == "POST":
        print(request.POST)
        data = request.POST
        stats = Calculator()

        full_data_extract(stats, data)

        result = stats.total_damage

        print(result)

        context = {"result": result, "stats": stats, "reaction": data.get("reaction", "Null"), "arts": data.get("arts")}

        return render(request, "estimation/estimation.html", context=context)


@login_required
def estimation_save(request):
    if request.method == "POST":
        print(request.POST.get("action"))
        data = request.POST
        if data.get("template_name"):
            name = data.get("template_name")
        else:
            name = datetime.now()

        stats = StatModel.objects.get_or_create(name=name, user_id=request.user)[0]

        full_data_extract(stats, data)
        stats.save()

        return redirect("Estimation:estimation_templates")


@login_required
def template_view(request):
    templates = StatModel.objects.filter(user_id=request.user.id)
    context = {"templates": templates}
    return render(request, "estimation/my_templates.html", context=context)


def delete_template_view(request, pk):
    if request.method == "GET":
        context = {"stats": StatModel.objects.get(pk=pk)}

        return render(request, "estimation/template_delete.html", context=context)
    if request.method == "POST":
        stats = StatModel.objects.get(pk=pk)
        stats.delete()
        return redirect("Estimation:estimation_templates")
