from django.urls import path
from . import views

app_name = 'task'


urlpatterns = [
    path('', views.task_list, name='task_list'),

]
