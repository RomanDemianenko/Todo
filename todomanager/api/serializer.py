from rest_framework import serializers

from todomanager.models import TodoManager


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoManager
        fields = '__all__'
