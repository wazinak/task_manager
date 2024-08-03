from django.urls import path, re_path
from .views import TaskList, TaskDetail, UserTasks
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    re_path('^user/(?P<username>.+)/$', UserTasks.as_view(), name='user_tasks'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
