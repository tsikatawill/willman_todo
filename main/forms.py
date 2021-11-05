from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'first_name', 'last_name'
    ]
        
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'owner']
        
class EditTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        