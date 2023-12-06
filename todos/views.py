from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class ListAPITodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailAPITodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreatAPITodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
