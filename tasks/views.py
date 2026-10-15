"""Interfaz web original, ahora conectada a la base de datos."""
from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task


def task_manager(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        task = form.save()
        messages.success(request, "Tarea guardada correctamente en la base de datos.")
        return redirect(f"/?added={task.pk}")

    stats = Task.objects.aggregate(
        total=Count("pk"), completed=Count("pk", filter=Q(completed=True))
    )
    total = stats["total"]
    completed = stats["completed"]

    # Se muestra el resultado recién registrado sin volver a ejecutar el POST.
    added_id = request.GET.get("added", "")
    result = Task.objects.filter(pk=added_id).first() if added_id.isdecimal() else None
    return render(request, "tasks/task_manager.html", {
        "form": form,
        "tasks": Task.objects.all(),
        "task_result": result,
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": total - completed,
        "completion_percentage": round(completed * 100 / total, 1) if total else 0,
    })


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Tarea actualizada correctamente.")
        return redirect("task_manager")
    return render(request, "tasks/task_edit.html", {"form": form, "task": task})


@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, "Tarea eliminada correctamente.")
    return redirect("task_manager")


def about(request):
    return render(request, "tasks/about.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)
