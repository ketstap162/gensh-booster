from django.urls import path

from GenshinStorage.views import index, storage_view, char_detail_view

urlpatterns = [
    path("", index, name="index"),
    path("storage", storage_view, name="storage"),
    path("storage/<int:pk>", char_detail_view, name="char-detail"),
]


app_name = "GenshinStorage"
