from django.contrib import admin
from django.urls import include, path
from tasks.views import custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]

handler404 = custom_404
