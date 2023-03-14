from django.forms import ModelForm
from django import forms
from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )

class NoteForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea)
