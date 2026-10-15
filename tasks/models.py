"""Modelo persistente basado en los campos de la Evaluación 1."""
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = "Alta", "Alta"
        MEDIUM = "Media", "Media"
        LOW = "Baja", "Baja"

    name = models.CharField("nombre", max_length=100)
    priority = models.CharField(
        "prioridad", max_length=5, choices=Priority.choices, default=Priority.MEDIUM
    )
    hours = models.DecimalField(
        "horas estimadas", max_digits=6, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))], default=Decimal("1.00")
    )
    completed = models.BooleanField("completada", default=False)
    created_at = models.DateTimeField("creada", auto_now_add=True)
    updated_at = models.DateTimeField("actualizada", auto_now=True)

    class Meta:
        ordering = ["-created_at", "-id"]
        verbose_name = "tarea"
        verbose_name_plural = "tareas"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(hours__gte=0), name="task_hours_non_negative"
            )
        ]

    def __str__(self):
        return self.name

    @property
    def status(self):
        return "Completada" if self.completed else "Pendiente"

    @property
    def priority_message(self):
        if self.priority == self.Priority.HIGH:
            return "Requiere atención prioritaria."
        if self.priority == self.Priority.MEDIUM:
            return "Tiene una prioridad intermedia."
        return "Puede realizarse cuando exista disponibilidad."

    @property
    def workload(self):
        if self.hours > 4:
            return "Carga alta"
        if self.hours >= 2:
            return "Carga media"
        return "Carga baja"
