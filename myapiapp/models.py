from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Actions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='actions')
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Action'
