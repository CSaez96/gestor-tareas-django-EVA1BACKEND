# Migración inicial del modelo Task para Evaluación 2.
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="nombre")),
                ("priority", models.CharField(choices=[("Alta", "Alta"), ("Media", "Media"), ("Baja", "Baja")], default="Media", max_length=5, verbose_name="prioridad")),
                ("hours", models.DecimalField(decimal_places=2, default=Decimal("1.00"), max_digits=6, validators=[MinValueValidator(Decimal("0.00"))], verbose_name="horas estimadas")),
                ("completed", models.BooleanField(default=False, verbose_name="completada")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="creada")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="actualizada")),
            ],
            options={"verbose_name": "tarea", "verbose_name_plural": "tareas", "ordering": ["-created_at", "-id"]},
        ),
        migrations.AddConstraint(
            model_name="task",
            constraint=models.CheckConstraint(condition=models.Q(hours__gte=0), name="task_hours_non_negative"),
        ),
    ]
