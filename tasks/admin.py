from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "priority", "hours", "completed", "created_at")
    list_filter = ("priority", "completed")
    search_fields = ("name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
