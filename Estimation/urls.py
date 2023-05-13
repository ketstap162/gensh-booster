from django.urls import path

from Estimation.views import estimation_view, template_view

urlpatterns = [
    path("", estimation_view, name="estimation_view"),
    path("templates", template_view, name="estimation_templates")
]


app_name = "Estimation"
