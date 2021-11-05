from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-todos/<str:pk>/', views.todos, name='todos'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('delete-todo/<str:pk>/', views.deleteTodo, name='delete-todo'),
    path('edit-todo/<str:pk>/', views.editTodo, name='edit-todo'),
]