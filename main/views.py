from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from .models import *

from django.core.paginator import Paginator

# Create your views here.
def todos(request, pk):
    loggedInUser = User.objects.get(username=pk)
    todos = Todo.objects.filter(owner=loggedInUser).order_by('completed')
    form = TodoForm()
    
    p = Paginator(todos, 3)
    page = request.GET.get('page')
    
    if request.method == 'POST':
        try:
            data = {
                'title': request.POST["new_todo"],
                'owner': request.user,
                'completed': False
            }
            form = TodoForm(data)
            form.save()
            messages.success(request, 'Todo added succesfuly')
        except Exception as e:
            messages.error(request, 'Error adding todo')
            
    todos = p.get_page(page)        
    context = {'todos': todos}
    return render(request, 'main/todos.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, 'Account successfully created for ' + str(username.upper()))
            return redirect('login')
    context = {'form': form}
    return render(request, 'main/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in')
            return redirect(f'/user-todos/{request.user}/')
        else:
            messages.info(request, 'Wrong username and/or password')
   
    context = {}
    return render(request, 'main/login.html', context)

def home(request):
    return render(request, 'main/home.html')

def signOut(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

def deleteTodo(request, pk):
    selected_todo = Todo.objects.get(id=pk)
    context = {'todo': selected_todo}
    
    if request.method=='POST':
        selected_todo.delete()
        messages.success(request, f'{selected_todo} has been deleted successfully')
        return redirect(f'/user-todos/{request.user}')
    
   
    return render(request, 'main/confirm-delete.html', context)

def editTodo(request, pk):
    selected_todo = Todo.objects.get(id=pk)
    form = EditTodoForm(instance=selected_todo)
    if request.method=='POST':
        
        form = EditTodoForm(request.POST, instance=selected_todo)
        if form.is_valid():
            form.save()
            messages.success(request, f'{selected_todo} has been edited successfully')
            return redirect(f'/user-todos/{request.user}/')
        else:
            messages.info(request, 'Error saving TODO')
            
    context = {'todo': selected_todo, 'form': form}
    return render(request, 'main/edit-todo.html', context)