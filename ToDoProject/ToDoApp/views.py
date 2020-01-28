from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import ToDo
from datetime import datetime


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ToDoApp/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return the To Do items"""
        return ToDo.objects.order_by('created_date')


class DetailView(generic.DetailView):
    template_name = 'ToDoApp/detail.html'
    model = ToDo


class DeleteToDoView(generic.DetailView):
    template_name = 'ToDoApp/delete_todo_modal.html'
    model = ToDo


class CreateToDoModalView(generic.ListView):
    template_name = 'ToDoApp/create_todo_modal.html'
    model = ToDo


def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('new_title')
        description = request.POST.get('new_description')
        state = eval(request.POST.get('new_state').capitalize())

        ToDo.objects.create(
            id=(1 if ToDo.objects.count() == 0 else ToDo.objects.latest('id').id + 1),
            title=title,
            description=description,
            state=state,
            created_date=datetime.now().strftime('%Y-%m-%d %H:%M'),
        )

        return HttpResponseRedirect('/ToDoApp/')


def delete_todo(request, pk):
    if request.method == 'POST':
        obj = ToDo.objects.get(id=pk)
        obj.delete()

    return HttpResponseRedirect('/ToDoApp/')


def change_status(request, pk):
    if request.method == 'POST':
        obj = ToDo.objects.get(id=pk)
        obj.state = (not obj.state)
        obj.save()

    return HttpResponseRedirect('/ToDoApp/')


