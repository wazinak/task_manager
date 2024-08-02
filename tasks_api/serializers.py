from rest_framework import serializers
from tasks.models import Task, TaskPermission


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPermission
        fields = '__all__'
