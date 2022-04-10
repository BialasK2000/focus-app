import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import DateInput, VisibilityForm, UpdateUserForm, UpdateProfileForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django import forms


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-profile')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profilepage.html', {'user_form': user_form, 'profile_form': profile_form})


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

        quotes = ['"Logic will take you from A to B. Imagination will take you everywhere."',
                  '"Hate is a lack of imagination."',
                  '"I am a brain, Watson. The rest of me is a mere appendix."',
                  '"Beauty you are born with, but brains you earn."',
                  '"I not only use all the brains that I have, but all I can borrow."',
                  '"It’s not that I’m so smart, it’s just that I stay with problems longer."',
                  '"Any fool can know. The point is to understand."',
                  '"The measure of intelligence is the ability to change."',
                  '"Try not to become a person of success, but rather try to become a person of value."',
                  '"Education is not the learning of the facts, but the training of the mind to think."',
                  '"Spread love everywhere you go. Let no one ever come to you without leaving happier."',
                  '"Always remember that you are absolutely unique. Just like everyone else."',
                  '"Do not judge each day by the harvest you reap but by the seeds that you plant."',
                  '"The future belongs to those who believe in the beauty of their dreams."',
                  '"Tell me and I forget. Teach me and I remember. Involve me and I learn."',
                  '"It is during our darkest moments that we must focus to see the light."',
                  '"Life is a long lesson in humility."',
                  '"Success usually comes to those who are too busy to be looking for it."',
                  '"The way to get started is to quit talking and begin doing."',
                  '"If you really look closely, most overnight successes took a long time."',
                  '"The road to success and the road to failure are almost exactly the same."',
                  '"If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work."',
                  '"Before anything else, preparation is the key to success."',
                  ]

        context['random_quote'] = random.choice(quotes)

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

    def get_form(self):
        form = super(CreateTaskView, self).get_form()
        form.fields['deadline'].widget = DateInput()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'deadline', 'status']
    template_name = "createtasks.html"
    success_url = reverse_lazy('main-tasks')

    def get_form(self):
        form = super(TaskUpdateView, self).get_form()
        form.fields['deadline'].widget = DateInput()
        return form


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "deletetasks.html"
    success_url = reverse_lazy('main-tasks')


class TaskInvisibleView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = VisibilityForm
    template_name = "invisibletask.html"
    success_url = reverse_lazy('main-tasks')


class DeletedTasksView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "completedlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(status=False).count()

        search_input = self.request.GET.get('search_bar') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(name__icontains=search_input)

        context['search_input'] = search_input

        return context
