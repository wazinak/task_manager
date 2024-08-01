from django.shortcuts import render, get_object_or_404
from .models import *


def task_list(request):
    tasks = Task.objects.filter(creator=request.user)
    return render(request, 'list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail.html', {'task': task})
