from django import forms
from .models import Task, Profile

from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class VisibilityForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['visible']
        labels = {
            'visible': ''
        }

    def __init__(self, *args, **kwargs):
        super(VisibilityForm, self).__init__(*args, **kwargs)
        self.fields['visible'].widget.attrs.update({'class': 'niewidka'})


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
