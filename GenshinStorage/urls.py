from django.urls import path

from GenshinStorage.views import index, storage

urlpatterns = [
    path("", index, name="index"),
    path("storage", storage, name="storage")
]


app_name = "GenshinStorage"
