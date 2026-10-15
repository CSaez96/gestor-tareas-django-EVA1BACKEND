"""ModelViewSet incorpora list, retrieve, create, update, partial_update y destroy."""
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
