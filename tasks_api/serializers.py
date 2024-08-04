from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'creator',
        )

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
