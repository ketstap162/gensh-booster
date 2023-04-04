from django.shortcuts import render

from GenshinStorage.models import Post, Character


def index(request):
    """View function for the home page of the site."""

    num_visits = 1 + request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits
    context = {
        "posts": Post.objects.all(),
        "num_visits": num_visits
    }

    return render(request, "main/index.html", context=context)


def storage(request):
    """View function for the Storage section."""

    context = {
        "chars": Character.objects.all()
    }
    return render(request, "storage/storage.html", context=context)
