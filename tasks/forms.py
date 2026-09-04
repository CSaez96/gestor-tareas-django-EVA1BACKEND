from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(
        label="Nombre de la tarea",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ej. Estudiar Django"}),
    )
    priority = forms.ChoiceField(
        label="Prioridad",
        choices=[
            ("Alta", "Alta"),
            ("Media", "Media"),
            ("Baja", "Baja"),
        ],
        initial="Media",
    )
    hours = forms.FloatField(
        label="Horas estimadas",
        min_value=0,
        initial=1,
    )
    completed = forms.BooleanField(
        label="Tarea completada",
        required=False,
    )
