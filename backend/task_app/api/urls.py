from django.urls import path, include
from task_app.api.views import TaskAV, TaskDetailsAV

urlpatterns = [
    path('list/', TaskAV.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailsAV.as_view(), name='task-details'),
]