from django.urls import path

from . import views

app_name = 'ToDoApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('delete_todo_modal/<int:pk>/', views.DeleteToDoView.as_view(), name='delete_todo_modal'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('create_todo_modal/', views.CreateToDoModalView.as_view(), name='create_todo_modal'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('change_status/<int:pk>/', views.change_status, name='change_status'),
]