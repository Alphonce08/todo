from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Todo(models.Model):
    #username = models.CharField(max_length=30, blank=True, null=True)
    #password = models.IntegerField(max_length=30, blank=True, null=True)
    task = models.TextField(max_length=300)
    start_at = models.DateTimeField(blank=True,null=True)
    complete_at = models.DateTimeField(blank=True,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    

    def __str__(self):
        return f'DO: {self.task }'
    
   