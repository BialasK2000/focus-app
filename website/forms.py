from django import forms
from .models import Task


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
