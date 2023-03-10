from rest_framework import serializers
from task_app.models import Task, List

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'list', 'description', 'completed', 'completeBy', 'created', 'updated']
        
class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = List
        fields = ['id', 'name', 'description', 'tasks']