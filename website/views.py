from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task


class MainTasksView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "maintasks.html"


class DetailTaskView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "detailtasks.html"


class CreateTaskView(CreateView):
    model = Task
    fields = '__all__'
    template_name = "createtasks.html"
    success_url = reverse_lazy('main-tasks')

