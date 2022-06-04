from pickle import TRUE
from sys import api_version
from urllib import response
#from urllib import response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import taskModelSerializer
from task.models import tasks

from task import serializers


class taskAPIView(APIView):
    serializer_class = taskModelSerializer

    def get_queryset(self):
        queryset = tasks.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = taskModelSerializer(tasks, many=True)

        return Response(serializer.data)


class taskPostView(APIView):
    serializer_class = taskModelSerializer
    def post(self, request, *args, **kwargs):

        task_info = request.data

        new_task = tasks.objects.create(name=task_info["name"],
                                        description=task_info["description"],
                                        email=task_info["email"])

        new_task.save()

        serializer = taskModelSerializer(new_task)

        return Response(serializer.data)