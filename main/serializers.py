from rest_framework import serializers
from .models import TasksModel

class TaskModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TasksModel
        exclude = ['created_at']
