from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class MainTasksView(ListView):
    model = Task
    template_name = "maintasks.html"
