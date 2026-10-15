from django.contrib import admin
from django.urls import include, path
from tasks.views import custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("tasks.urls")),
]

handler404 = custom_404
