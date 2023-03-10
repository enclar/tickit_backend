from django.urls import path, include
from task_app.api.views import TaskList, TaskDetail, ListList, ListDetail

urlpatterns = [
    path('task/list/', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('list/list/', ListList.as_view(), name='list-list'),
    path('list/<int:pk>/', ListDetail.as_view(), name='task-details'),
]