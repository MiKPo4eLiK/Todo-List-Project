from django import forms
from .models import Task, Tags

class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    deadline_datetime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    class Meta:
        model = Task
        fields = ["content", "deadline_datetime", "tags", "is_done"]


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = "__all__"
