from django.db import models
from accounts.models import User
from django.utils import timezone


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='time created', default=timezone.now)

    def __str__(self):
        return self.name


class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(verbose_name='time created', default=timezone.now)

    def __str__(self):
        return '{} Action'.format(self.project.name)
