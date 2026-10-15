from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "priority", "hours", "completed")
        labels = {
            "name": "Nombre de la tarea",
            "priority": "Prioridad",
            "hours": "Horas estimadas",
            "completed": "Tarea completada",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ej. Estudiar Django"}),
            "hours": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
        }

    def clean_name(self):
        value = self.cleaned_data["name"].strip()
        if not value:
            raise forms.ValidationError("El nombre no puede estar vacío.")
        return value
