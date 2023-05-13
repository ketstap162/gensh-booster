from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from gensh_booster.views import register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', register_view, name='register'),
    path("", include("GenshinStorage.urls", namespace="GStorage")),
    path("estimation/", include("Estimation.urls", namespace="Estimation")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
