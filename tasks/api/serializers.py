"""Representación JSON del modelo Task."""
from decimal import Decimal

from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    hours = serializers.DecimalField(
        max_digits=6, decimal_places=2, min_value=Decimal("0.00")
    )

    class Meta:
        model = Task
        fields = (
            "id", "name", "priority", "hours", "completed", "created_at", "updated_at"
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_name(self, value):
        name = value.strip()
        if not name:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return name
