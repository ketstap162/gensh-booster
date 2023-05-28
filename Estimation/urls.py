from django.urls import path

from Estimation.views import estimation_view, template_view, estimation_save, delete_template_view

urlpatterns = [
    path("", estimation_view, name="estimation_view"),
    path("save", estimation_save, name="estimation_save"),
    path("templates/", template_view, name="estimation_templates"),
    path("", delete_template_view, name="delete_template"),
]


app_name = "Estimation"
