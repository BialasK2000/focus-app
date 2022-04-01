from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class BetaLoginView(LoginView):
    fields = "__all__"
    template_name = "login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("main-tasks")


class BetaRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main-tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(BetaRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main-tasks')
        else:
            return super(BetaRegisterView, self).get(*args, **kwargs)

class BetaLogoutView(LogoutView):
    next_page = "login"


class MainTasksView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "maintasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(status=False).count()

        search_input = self.request.GET.get('search_bar') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(name__icontains=search_input)

        context['search_input'] = search_input

        return context


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "detailtasks.html"


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'deadline', 'status']
    template_name = "createtasks.html"
    success_url = reverse_lazy('main-tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'deadline', 'status']
    template_name = "createtasks.html"
    success_url = reverse_lazy('main-tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "deletetasks.html"
    success_url = reverse_lazy('main-tasks')