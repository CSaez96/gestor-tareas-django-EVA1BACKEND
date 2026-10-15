from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_manager, name="task_manager"),
    path("about/", views.about, name="about"),
    path("tasks/<int:pk>/edit/", views.edit_task, name="task_edit"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="task_delete"),
]
