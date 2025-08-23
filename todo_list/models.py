from django.db import models
from django.urls import reverse

class Tags(models.Model):
    """
    Model representing a task tag.
    """
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Task(models.Model):
    """
    Model representing a single task in the to-do list.
    """
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created_datetime"]

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("todo_list:index")
