from django.urls import path
from .views import ListAPITodo, DetailAPITodo

urlpatterns = [
    path("", ListAPITodo.as_view(), name="todo_list"),
    path("<int:pk>/", DetailAPITodo.as_view(), name="todo_detail"),
]
