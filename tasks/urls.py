from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_manager, name="task_manager"),
    path("about/", views.about, name="about"),
]
