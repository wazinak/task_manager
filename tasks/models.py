from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskPermission(models.Model):
    READ = 'R'
    UPDATE = 'U'
    DELETE = 'D'

    PERMISSION_CHOICES = [
        (READ, 'Прочитано'),
        (UPDATE, 'Обновить'),
        (DELETE, 'Удалить'),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.CharField(max_length=1, choices=PERMISSION_CHOICES)

    class Meta:
        unique_together = ('task', 'user', 'permission')

    def __str__(self):
        return f'{self.user.username} - {self.permission} for {self.task.title}'
