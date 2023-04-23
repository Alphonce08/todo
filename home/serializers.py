from rest_framework import serializers
from .models import Todo

class Todoserializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','task','start_at', 'complete_at')