from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    ToggleTaskStatusView
)

app_name = "todo_list"

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", ToggleTaskStatusView.as_view(), name="task-toggle"),

    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag-delete"),
]
