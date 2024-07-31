from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task, TaskPermission
from.serializers import TaskSerializer, TaskPermissionSerializer

# вереемся к задачам и их правам
