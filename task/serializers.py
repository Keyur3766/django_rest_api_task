from rest_framework import serializers

from task.models import tasks


class taskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'