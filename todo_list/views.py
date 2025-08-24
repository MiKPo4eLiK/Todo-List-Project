from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Task, Tags
from .forms import TaskForm, TagsForm

class TaskListView(ListView):
    model = Task
    template_name = "todo_list/index.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:index")

class TagsListView(ListView):
    model = Tags
    template_name = "todo_list/tag_list.html"
    context_object_name = "tags"

class TagsCreateView(CreateView):
    model = Tags
    form_class = TagsForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")

class TagsUpdateView(UpdateView):
    model = Tags
    form_class = TagsForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")

class TagsDeleteView(DeleteView):
    model = Tags
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")

class ToggleTaskStatusView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('todo_list:index')
