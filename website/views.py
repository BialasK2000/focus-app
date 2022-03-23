from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class BetaLoginView(LoginView):
    fields = "__all__"
    template_name = "login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("main-tasks")


class BetaLogoutView(LogoutView):
    next_page = "login"


class MainTasksView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "maintasks.html"


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "detailtasks.html"


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    template_name = "createtasks.html"
    success_url = reverse_lazy('main-tasks')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = "createtasks.html"
    success_url = reverse_lazy('main-tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "deletetasks.html"
    success_url = reverse_lazy('main-tasks')