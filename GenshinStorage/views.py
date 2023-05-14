from django.shortcuts import render

from GenshinStorage.models import Post, Character, Element


def index(request):
    """View function for the home page of the site."""

    num_visits = 1 + request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits
    context = {"posts": Post.objects.all(), "num_visits": num_visits}

    return render(request, "main/index.html", context=context)


def storage_view(request):
    """View function for the Storage section."""

    context = {
        "elements": Element.objects.all(),
        "chars": Character.objects.select_related("element", "weapon", "location").order_by("full_name"),
    }

    element_filter = request.GET.get("filter")

    if element_filter:
        context["chars"] = context["chars"].filter(element__name=element_filter)

    return render(request, "storage/storage.html", context=context)


def char_detail_view(request, pk):
    context = {
        "char": Character.objects.get(pk=pk),
    }

    return render(request, "storage/char_detail.html", context=context)
