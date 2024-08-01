from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Задача")
    description = models.TextField(verbose_name='Описание')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.title


class TaskPermission(models.Model):
    READ = 'read'
    UPDATE = 'update'
    PERMISSION_CHOICES = [
        (READ, 'ПРОСМОТР'),
        (UPDATE, 'ОБНОВЛЕНИЕ'),
    ]
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default=READ, verbose_name="Разрешение")

    class Meta:
        unique_together = ('task', 'user', 'permission')

    def __str__(self):
        return f'{self.user.username} - {self.permission} for {self.task.title}'