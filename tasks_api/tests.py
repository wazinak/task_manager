from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from tasks.models import Task
from .serializers import TaskSerializer


class TaskTestAPICase(APITestCase):
    def test_get(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        url = reverse('task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_serializer(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        task_1 = Task.objects.create(title='test',
                                     description='test',
                                     creator=user)
        data = TaskSerializer(task_1).data
        expected = {
            'id': task_1.id,
            'title': task_1.title,
            'description': task_1.description,
            'creator': task_1.creator.id,
        }
        self.assertEqual(data, expected)
