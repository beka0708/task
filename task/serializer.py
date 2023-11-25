from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    completed = serializers.BooleanField(default=False)


class TaskItemSerializer:
    class Meta:
        model = Task
        fields = '__all__'
