from rest_framework import serializers
from .models import TodoModel


# Serializing TodoModel
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
