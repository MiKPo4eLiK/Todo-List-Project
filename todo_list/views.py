from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Task, Tags
from .forms import TaskForm, TagsForm

class TaskListView(ListView):
    """View for listing all tasks."""
    model = Task
    template_name = "todo_list/index.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView):
    """View for creating a new task."""
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")

class TaskUpdateView(UpdateView):
    """View for updating an existing task."""
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")

class TaskDeleteView(DeleteView):
    """View for deleting a task."""
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:index")

class TagsListView(ListView):
    """View for listing all tags."""
    model = Tags
    template_name = "todo_list/tag_list.html"
    context_object_name = "tags"

class TagsCreateView(CreateView):
    """View for creating a new tag."""
    model = Tags
    form_class = TagsForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")

class TagsUpdateView(UpdateView):
    """View for updating an existing tag."""
    model = Tags
    form_class = TagsForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")

class TagsDeleteView(DeleteView):
    """View for deleting a tag."""
    model = Tags
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")

def toggle_task_status(request, pk):
    """Toggles the 'is_done' status of a task."""
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse("todo_list:index"))
