from django.urls import path, include
from task_app.api.views import TaskList, TaskDetail

urlpatterns = [
    path('list/', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task-details'),
]