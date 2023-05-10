from django.urls import path

from Estimation.views import estimation_view

urlpatterns = [
    path("", estimation_view, name="estimation_view"),
]


app_name = "Estimation"
