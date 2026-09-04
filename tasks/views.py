from django.shortcuts import render
from .forms import TaskForm


# Datos de ejemplo mantenidos en memoria durante la ejecución.
TASKS = [
    {
        "name": "Preparar evaluación",
        "priority": "Alta",
        "hours": 3.0,
        "completed": False,
    },
    {
        "name": "Revisar README",
        "priority": "Media",
        "hours": 1.5,
        "completed": True,
    },
    {
        "name": "Subir proyecto a GitHub",
        "priority": "Alta",
        "hours": 1.0,
        "completed": False,
    },
]


def task_manager(request):
    message = ""
    task_result = None
    form = TaskForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"].strip()
        priority = form.cleaned_data["priority"]
        hours = form.cleaned_data["hours"]
        completed = form.cleaned_data["completed"]

        if completed:
            status = "Completada"
        else:
            status = "Pendiente"

        if priority == "Alta":
            priority_message = "Requiere atención prioritaria."
        elif priority == "Media":
            priority_message = "Tiene una prioridad intermedia."
        else:
            priority_message = "Puede realizarse cuando exista disponibilidad."

        if hours > 4:
            workload = "Carga alta"
        elif hours >= 2:
            workload = "Carga media"
        else:
            workload = "Carga baja"

        task_result = {
            "name": name,
            "priority": priority,
            "hours": hours,
            "completed": completed,
            "status": status,
            "priority_message": priority_message,
            "workload": workload,
        }

        TASKS.append({
            "name": name,
            "priority": priority,
            "hours": hours,
            "completed": completed,
        })

        message = "Tarea procesada correctamente."

    total_tasks = len(TASKS)
    completed_tasks = 0

    for task in TASKS:
        if task["completed"]:
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    if total_tasks > 0:
        completion_percentage = (completed_tasks / total_tasks) * 100
    else:
        completion_percentage = 0

    context = {
        "form": form,
        "tasks": TASKS,
        "task_result": task_result,
        "message": message,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_percentage": round(completion_percentage, 1),
    }

    return render(request, "tasks/task_manager.html", context)


def about(request):
    return render(request, "tasks/about.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)
