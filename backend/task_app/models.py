from django.db import models
import datetime

# List Model
class List(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.name
    
# Task Model
class Task(models.Model):
    list = models.ForeignKey(List, related_name="tasks", on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    completeBy = models.DateField()
    
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.name