from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from todomanager.api.serializer import TodoSerializer
from todomanager.models import TodoManager


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoManager.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        course = get_object_or_404(TodoManager.objects.filter(id=pk))
        serializer = TodoSerializer(instance=course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pk = self.kwargs.get('pk')
        course = get_object_or_404(TodoManager.objects.filter(id=pk))
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False)
    def notdone(self, request, *args, **kwargs):
        queryset = self.queryset.filter(done=False)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)