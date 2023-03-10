from rest_framework import serializers
from task_app.models import Task, List

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'description']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'list', 'description', 'completed', 'completeBy', 'created', 'updated']