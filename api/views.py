from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import TaskModelSerializer
from main.models import TasksModel


class ToDoModelView(APIView):
    def get(self, request):
        qs = TasksModel.objects.all()
        serializer = TaskModelSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskModelSerializer.(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'okay'})
        return Response({'error': "Ma'lumotlar to'liq emas!"})


class TaskViews(APIView):
    def get(self, request):
        return Response({'ok': 'hello'})
