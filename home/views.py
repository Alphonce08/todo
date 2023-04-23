from rest_framework import viewsets
from .models import Todo
from .serializers import Todoserializers


class TodoviewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers
