from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 255, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    